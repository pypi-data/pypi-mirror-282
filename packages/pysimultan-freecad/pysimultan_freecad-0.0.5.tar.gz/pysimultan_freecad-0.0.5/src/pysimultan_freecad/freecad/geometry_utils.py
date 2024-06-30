import os
import tempfile
import trimesh

from .logger import logger

try:
    import FreeCAD
except ModuleNotFoundError:
    import sys

    sys.path.append('/tmp/squashfs-root/usr/lib/python3.10/site-packages/')
    sys.path.append('/tmp/squashfs-root/usr/lib/')
    sys.path.append('/usr/lib/python3.10/')
    sys.path.append('/usr/lib/python3/dist-packages')
    import FreeCAD

# import Draft
import Part as FCPart
# import Mesh
import MeshPart

from FreeCAD import Base


App = FreeCAD


def create_fc_vertex(vertex):
    return FCPart.Point(Base.Vector(vertex.position[0], vertex.position[1], vertex.position[2]))


def create_fc_edge(edge):

    if edge.vertices[0].fc_inst == edge.vertices[1].fc_inst:
        edge._collapsed = True
        return None
    else:
        edge._collapsed = False
        if edge.type == 'arc':
            return FCPart.Edge(FCPart.Arc(Base.Vector(edge.vertices[0].position),
                                          Base.Vector(edge.interpolation_points[0]),
                                          Base.Vector(edge.vertices[1].position))
                               )
        elif edge.type in ['line', None]:
            return FCPart.Edge(FCPart.LineSegment(Base.Vector(edge.vertices[0].position),
                                                  Base.Vector(edge.vertices[1].position)))


def create_fc_edge_loop(edge_loop):
    edges = [x.fc_inst for x in edge_loop.edges if x.fc_inst is not None]
    if edges.__len__() < 3:
        return None
    else:
        try:
            face_wire = FCPart.Wire(edges)
            return face_wire
        except Exception as e:
            logger.info(f'Could not generate face wire for face:\n{edge_loop.id}')
            raise e


def create_fc_face(face):

    if face.extruded:
        # https://forum.freecadweb.org/viewtopic.php?t=21636

        # save_fcstd([x.fc_edge for x in self.extruded], f'/tmp/extrude_edges_face{self.id}')
        # ex_wire = FCPart.Wire([x.fc_edge for x in self.extruded])
        # save_fcstd([ex_wire], f'/tmp/extrude_wire{self.id}')

        doc = App.newDocument()
        sweep = doc.addObject('Part::Sweep', 'Sweep')
        section0 = doc.addObject("Part::Feature", f'section0')
        section0.Shape = FCPart.Wire(face.extruded[0].fc_edge)
        section1 = doc.addObject("Part::Feature", f'section1')
        section1.Shape = FCPart.Wire(face.extruded[1].fc_edge)
        spine = doc.addObject("Part::Feature", f'spine')
        spine.Shape = FCPart.Wire(face.extruded[2].fc_edge)

        sweep.Sections = [section0, section1]
        sweep.Spine = spine
        sweep.SolidMaterial = False
        sweep.Frenet = False

        doc.recompute()

        fc_face = sweep.Shape
    else:
        try:
            fc_face = FCPart.Face([face.boundary.fc_inst, *[x.fc_inst for x in face.holes]])
        except FCPart.OCCError as e:
            logger.debug(f'Could not generate face for face:\n{face.id}: {e}')
            if e.args[0] == 'Not planar':
                logger.debug(f'Face {face.id} is not planar')
                fc_face = FCPart.makeFilledFace(face.boundary.fc_inst.OrderedEdges)
            else:
                raise e

    if fc_face.Area < 1e-3:
        logger.warning(f'Face {face.id} area very small: {face.Area}')

    return fc_face


def create_fc_volume(volume):
    logger.info(f'Generating solid from faces: {volume.name} {volume.id}')

    faces = []
    [faces.extend(x.fc_inst.Faces) for x in volume.faces]
    shell = FCPart.makeShell(faces)
    shell.sewShape()
    shell.fix(1e-7, 1e-7, 1e-7)
    solid = FCPart.Solid(shell)

    if not solid.isClosed():
        logger.error(f'SolidMaterial {volume.id}: solid is not closed')

    doc = App.newDocument()
    __o__ = doc.addObject("Part::Feature", f'{str(volume.id)}')
    __o__.Label = f'{str(volume.id)}'
    __o__.Shape = solid
    # logger.debug(f'        doc time: {time.time() - doc_start_time} s')

    logger.debug(f'Successfully finished generation of solid from faces: {volume.id}')

    return __o__


def create_stl_file(face, of=False, scale_to_m=True):
    # logger.debug(f'creating stl string for face {face.id}...')

    if of:
        face_name = face.txt_id
    else:
        face_name = str(face.id)

    try:
        fd, tmp_file = tempfile.mkstemp(suffix='.ast')
        os.close(fd)

        mesh_shp = MeshPart.meshFromShape(face.fc_inst,
                                          LinearDeflection=face.linear_deflection,
                                          AngularDeflection=face.angular_deflection)
        if scale_to_m:
            mat = FreeCAD.Matrix()
            mat.A11 = 0.001  # make the objects two times bigger
            mat.A22 = 0.001
            mat.A33 = 0.001

            mesh_shp.transform(mat)

        mesh_shp.write(tmp_file)

        with open(tmp_file, encoding="utf8") as file:
            content = file.readlines()
            content[0] = f'solid {face_name}\n'
            content[-1] = f'endsolid {face_name}\n'

    except Exception as e:
        logger.error(f'error while creating stl string for face {face.id}:\n{e}')
    finally:
        try:
            os.remove(tmp_file, dir_fd=None)
        except FileNotFoundError as e:
            print(e)

    # logger.debug(f'    created stl string for face {face.id}...')

    return ''.join(content)


def save_volume_fcstd(volume, shape_type='solid'):
    """
    save as freecad document
    :param filename: full filename; example: '/tmp/test.FCStd'
    :param shape_type: 'solid', 'faces'
    """

    _, tmp_file = tempfile.mkstemp(suffix='.fcstd')

    doc = App.newDocument(f"SolidMaterial {volume.name}")
    if shape_type == 'solid':
        __o__ = doc.addObject("Part::Feature", f'SolidMaterial {volume.name} {volume.id}')
        __o__.Shape = volume.fc_inst.Shape
    elif shape_type == 'face':
        for face in volume.faces:
            __o__ = doc.addObject("Part::Face", f'Face {face.name} {face.id}')
            __o__.Shape = face.fc_inst.Shape
    doc.recompute()
    doc.saveCopy(tmp_file)

    # read and return file content
    with open(tmp_file, 'rb') as file:
        content = file.read()

    os.remove(tmp_file)

    return content


def calc_obb(pts):

    p = trimesh.points.PointCloud(pts)
    obb = p.bounding_box_oriented

    return obb


def create_face_stl_str(face, of=False, scale_to_m=True, linear_deflection=0.1, angular_deflection=0.5):

    if of:
        face_name = face.txt_id
    else:
        face_name = str(face.name)

    try:
        fd, tmp_file = tempfile.mkstemp(suffix='.ast')
        os.close(fd)

        mesh_shp = MeshPart.meshFromShape(face.fc_inst,
                                          LinearDeflection=linear_deflection,
                                          AngularDeflection=angular_deflection)
        if scale_to_m:
            mat = FreeCAD.Matrix()
            mat.A11 = 0.001  # make the objects two times bigger
            mat.A22 = 0.001
            mat.A33 = 0.001

            mesh_shp.transform(mat)

        # mesh_shp = MeshPart.meshFromShape(self.fc_face, MaxLength=1000)

        mesh_shp.write(tmp_file)

        with open(tmp_file, encoding="utf8") as file:
            content = file.readlines()
            content[0] = f'solid {face_name}\n'
            content[-1] = f'endsolid {face_name}\n'
    except Exception as e:
        logger.error(f'error while creating stl string for face {face.id}:\n{e}')
    finally:
        try:
            os.remove(tmp_file)
        except Exception as e:
            print(e)
            raise e

    # logger.debug(f'    created stl string for face {face.id}...')

    return ''.join(content)
