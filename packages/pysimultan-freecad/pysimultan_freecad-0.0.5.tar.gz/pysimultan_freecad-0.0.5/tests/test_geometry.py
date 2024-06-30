import os
import numpy as np
import logging

from PySimultan2 import DataModel
from pysimultan_freecad.src.pysimultan_freecad.mapping.mapper import mapper

logger = logging.getLogger(__name__)

project_dir = os.environ.get('PROJECT_DIR', '/simultan_projects')
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

new_data_model = DataModel.create_new_project(project_path=os.path.join(project_dir, 'test_geometry.simultan'),
                                              user_name='admin',
                                              password='admin')


def test_pipe_section(data_model):

    import FreeCAD
    import Part as FCPart
    from FreeCAD import Base

    def create_vertex(x=1, y=5, z=2):
        vertex = FCPart.Vertex(x, y, z)
        return vertex

    def create_face():
        vertices = np.array([[0, 0, 0],
                             [1, 0, 0],
                             [1, 1, 0],
                             [0, 1, 0],
                             ])
        points = [Base.Vector(row) for row in vertices]
        wire = FCPart.makePolygon([*points, points[0]])
        face = FCPart.Face(wire)
        return face

    def create_volume(move=10):
        vertices = np.array([[0, 0, 0],
                             [1, 0, 0],
                             [1, 1, 0],
                             [0, 1, 0],
                             [0, 0, 1],
                             [1, 0, 1],
                             [1, 1, 1],
                             [0, 1, 1],
                             ]) + move
        points = [Base.Vector(row) for row in vertices]
        faces = []
        faces.append(FCPart.Face(FCPart.makePolygon([points[0], points[1], points[2], points[3], points[0]])))
        faces.append(FCPart.Face(FCPart.makePolygon([points[4], points[5], points[6], points[7], points[4]])))
        faces.append(FCPart.Face(FCPart.makePolygon([points[0], points[1], points[5], points[4], points[0]])))
        faces.append(FCPart.Face(FCPart.makePolygon([points[1], points[2], points[6], points[5], points[1]])))
        faces.append(FCPart.Face(FCPart.makePolygon([points[2], points[3], points[7], points[6], points[2]])))
        faces.append(FCPart.Face(FCPart.makePolygon([points[3], points[0], points[4], points[7], points[3]])))
        shell = FCPart.makeShell(faces)
        solid = FCPart.Solid(shell)
        return solid

    def create_edge():
        vertices = np.array([[0, 0, 0],
                             [1, 5, 0],
                             ])
        points = [Base.Vector(row) for row in vertices]
        edge = FCPart.Edge(FCPart.makeLine(points[0], points[1]))
        return edge

    def create_wire():
        vertices = np.array([[0, 0, 0],
                             [1, 5, 0],
                             [2, 0, 0],
                             [3, 5, 0],
                             ])
        points = [Base.Vector(row) for row in vertices]
        edges = [FCPart.Edge(FCPart.makeLine(points[i], points[i+1])) for i in range(len(points)-1)]
        wire = FCPart.Wire(edges)
        return wire

    def create_closed_wire():
        vertices = np.array([[0, 0, 0],
                             [1, 5, 0],
                             [2, 0, 0],
                             [3, 5, 0],
                             [0, 0, 0],
                             ])
        points = [Base.Vector(row) for row in vertices]
        edges = [FCPart.Edge(FCPart.makeLine(points[i], points[i+1])) for i in range(len(points)-1)]
        wire = FCPart.Wire(edges)
        return wire

    FreeCADGeometry = mapper.get_mapped_class('free_cad_geometry')
    Edge = mapper.get_mapped_class('edge')
    Face = mapper.get_mapped_class('face')
    Solid = mapper.get_mapped_class('solid')
    Assembly = mapper.get_mapped_class('assembly')
    Wire = mapper.get_mapped_class('wire')
    Vertex = mapper.get_mapped_class('vertex')

    free_cad_geometry = FreeCADGeometry(name='free_cad_geometry',
                                        data_model=data_model)

    vertex1 = Vertex(name='vertex1',
                     fc_inst=create_vertex(0, 0, 0),
                     data_model=data_model,
                     fc_obj_file=free_cad_geometry)

    vertex2 = Vertex(name='vertex1',
                     fc_inst=create_vertex(3, 3, 2),
                     data_model=data_model,
                     fc_obj_file=free_cad_geometry)

    edge_fom_vertices = Edge(name='edge_fom_vertex',
                             vertices=[vertex1, vertex2],
                             data_model=data_model,
                             fc_obj_file=free_cad_geometry)

    edge1 = Edge(name='edge1',
                 fc_inst=create_edge(),
                 data_model=data_model,
                 fc_obj_file=free_cad_geometry)
    edge1.length

    edge1.vertices

    vertex = Vertex(name='vertex',
                    fc_inst=create_vertex(),
                    data_model=data_model,
                    fc_obj_file=free_cad_geometry)

    wire1 = Wire(name='wire1',
                 fc_inst=create_wire(),
                 data_model=data_model,
                 fc_obj_file=free_cad_geometry)

    wire2 = Wire(name='wire2',
                 fc_inst=create_closed_wire(),
                 data_model=data_model,
                 fc_obj_file=free_cad_geometry)

    face1 = Face(name='face1',
                 fc_inst=create_face(),
                 data_model=data_model,
                 fc_obj_file=free_cad_geometry)

    solid1 = Solid(name='solid1',
                   fc_inst=create_volume(),
                   data_model=data_model,
                   fc_obj_file=free_cad_geometry)

    solid2 = Solid(name='solid2',
                   fc_inst=create_volume(10),
                   data_model=data_model,
                   fc_obj_file=free_cad_geometry)

    solid3 = Solid(name='solid3',
                   fc_inst=create_volume(5),
                   data_model=data_model,
                   fc_obj_file=free_cad_geometry)

    solid1.is_closed

    assembly = Assembly(name='assembly',
                        data_model=data_model)

    assembly.add_geometry(solid1)
    assembly.add_geometry(solid2)

    assembly.add_feature(geometry=solid3,
                         feature='solid3')

    feat = assembly.get_feature('solid3')

    solid1.generate_faces()

    data_model.save()
    logger.debug('test_pipe_section')
    data_model.cleanup()


def load_test_data_model():
    mapper.clear()
    data_model = DataModel(project_path=os.path.join(project_dir, 'test_geometry.simultan'),
                           user_name='admin',
                           password='admin')
    # mapper.load_undefined = False
    mapper.load_undefined = True
    typed_data = data_model.get_typed_data(mapper=mapper,
                                           create_all=True)

    Edge = mapper.get_mapped_class('edge')
    Wire = mapper.get_mapped_class('wire')

    edge1 = Edge.cls_instances[0]
    edge1.length
    edge1.vertices

    wire1 = Wire.cls_instances[0]
    wire1.length

    Face = mapper.get_mapped_class('face')
    face_0 = Face.cls_instances[0]
    face_0.normal
    face_0.area

    Solid = mapper.get_mapped_class('solid')
    solid_0 = Solid.cls_instances[0]
    solid_0.faces

    Assembly = mapper.get_mapped_class('assembly')
    assembly_0 = Assembly.cls_instances[0]

    feat = assembly_0.features['solid3']
    assert isinstance(feat, Solid)

    data_model.save()
    data_model.cleanup()


if __name__ == '__main__':
    test_pipe_section(new_data_model)
    load_test_data_model()
    load_test_data_model()
