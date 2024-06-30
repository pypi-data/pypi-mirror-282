from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
import os
import itertools
import tempfile
import numpy as np
import gmsh
from .base_fc_geometry import BaseFCGeometry
from ..logger import logger
from ..tools import extract_to_meshio

import FreeCAD
import Part as FCPart
import MeshPart


class Face(BaseFCGeometry):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self._normal = kwargs.get('_normal', None)
        self._area = kwargs.get('_area', None)

        self.normal = kwargs.get('normal', None)
        self.fc_face = kwargs.get('fc_face', None)

    @property
    def fc_face(self) -> Union[FCPart.Shape, None]:
        return self.fc_inst

    @fc_face.setter
    def fc_face(self, value: Union[FCPart.Face, FCPart.Shape]):
        self.fc_inst = value

    @property
    def _fc_face(self) -> Union[FCPart.Shape, None]:
        return self._fc_inst

    @_fc_face.setter
    def _fc_face(self, value: Union[FCPart.Face, FCPart.Shape]) -> None:
        self._fc_face = value

    @property
    def area(self) -> float:
        self._area = self.fc_face.Area
        return self._area

    @area.setter
    def area(self, value: float) -> None:
        self._area = value

    @property
    def stl(self) -> str:
        return self.create_stl_str()

    @property
    def normal(self):
        if self._normal is None:
            vec = self.get_normal(self.fc_face.Vertexes[0].Point)
            self._normal = np.array([vec.x, vec.y, vec.z])
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value

    def update_area(self):
        self._area = self.fc_face.Area
        return self._area

    def update_normal(self):
        vec = self.get_normal(self.fc_face.Vertexes[0].Point)
        self._normal = np.array([vec.x, vec.y, vec.z])
        return self._normal

    def get_normal(self, point):
        uv = self.fc_face.Faces[0].Surface.parameter(point)
        nv = self.fc_face.Faces[0].normalAt(*uv)
        return nv.normalize()

    def create_stl_str(self, of=False, scale_to_m=True):
        """

        :param of: Export for openFoam
        :param scale_to_m: scale stl export to m instead of mm
        :return: stl string
        """

        # logger.debug(f'creating stl string for face {self.txt_id}...')
        # msh = MeshPart.meshFromShape(Shape=self.fc_face, MaxLength=1)

        face_name = self.txt_id

        try:
            fd, tmp_file = tempfile.mkstemp(suffix='.ast')
            os.close(fd)

            mesh_shp = MeshPart.meshFromShape(self.fc_face,
                                              LinearDeflection=self.linear_deflection,
                                              AngularDeflection=self.angular_deflection)
            if scale_to_m:
                mat = FreeCAD.Matrix()
                mat.A11 = 0.001     # make the objects two times bigger
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
            logger.error(f'error while creating stl string for face {self.id}:\n{e}')
        finally:
            try:
                os.remove(tmp_file)
            except Exception as e:
                print(e)
                raise e

        # logger.debug(f'    created stl string for face {self.id}...')

        return ''.join(content)

    def export_stl(self, filename):

        logger.debug(f'exporting stl for face {self.id}...')

        try:
            new_file = open(filename, 'w')
            new_file.writelines(self.stl)
            new_file.close()
            logger.debug(f'    finished stl export for face {self.id}')
        except Exception as e:
            logger.error(f'error while exporting .stl for face {self.id}:\n{e}')

    def create_mesh(self, max_length=99999999):
        mesh_shp = MeshPart.meshFromShape(Shape=self.fc_face,
                                          MaxLength=max_length)
        return mesh_shp

    def create_hex_g_mesh_2(self, lc=999999):

        if not self.fc_face.Wires[0].isClosed():
            raise Exception(f'Error creating hex mesh:\nFace {self} is not closed!')

        gmsh.initialize([])
        gmsh.model.add(f'{self.txt_id}')

        try:
            geo = gmsh.model.geo
            lc_p = lc
            counter = itertools.count(start=1)
            gm_vertices = [geo.addPoint(vertex.X, vertex.Y, vertex.Z, lc_p, next(counter)) for vertex in self.fc_face.Wires[0].OrderedVertexes]
            gmsh.model.geo.synchronize()

            edge_counter = itertools.count(start=1)
            gm_edges = [geo.addLine(i+1, i+2, next(edge_counter)) for i in range(gm_vertices.__len__()-1)]
            gm_edges.append(geo.addLine(gm_vertices[-1], 1, next(edge_counter)))
            gmsh.model.geo.synchronize()

            geo.addCurveLoop(gm_edges, 1)
            gmsh.model.geo.synchronize()

            geo.addPlaneSurface([1], 1)
            gmsh.model.geo.synchronize()

            gmsh.option.setNumber("General.Terminal", 0)
            gmsh.option.setNumber("Mesh.MeshSizeMin", 1)
            gmsh.option.setNumber("Mesh.MeshSizeMax", lc)

            # Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
            # (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
            # "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size fields
            # better - in particular size fields with large element size gradients:
            # gmsh.option.setNumber("Mesh.Algorithm", 5)

            # gmsh.option.setNumber("Mesh.Algorithm", 8)
            gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 2)
            gmsh.model.mesh.generate(2)
            gmsh.model.mesh.optimize('Relocate2D')

            # recombine to quad mesh
            # https://gitlab.onelab.info/gmsh/gmsh/-/issues/784
            gmsh.option.setNumber('General.Terminal', 0)
            # gmsh.model.mesh.setRecombine(2, 1)
            # gmsh.option.setNumber('SubdivisionAlgorithm ', 2)
            gmsh.model.mesh.recombine()
            # gmsh.model.mesh.recombine()
            mesh = extract_to_meshio()
            # mesh.write('/tmp/test.vtk')

        except Exception as e:
            logger.error(f'Error creating mesh for face {self.id}')
            raise e
        finally:
            gmsh.finalize()

        return mesh

    def create_hex_g_mesh(self, lc=999999):

        logger.warn(f'create_hex_g_mesh is deprecated. Use create_hex_g_mesh_2')

        if not self.fc_face.Wires[0].isClosed():
            raise Exception(f'Error creating hex mesh:\nFace {self} is not closed!')

        gmsh.initialize([])
        gmsh.model.add(f'{self.txt_id}')

        try:
            geo = gmsh.model.geo

            vertices = [tuple(x.Point) for x in self.fc_face.Vertexes]
            edges = [x for x in self.fc_face.Wires[0].OrderedEdges]

            vertex_lookup = dict(zip(vertices, range(vertices.__len__())))

            lc_p = lc
            for i, vertex in enumerate(vertices):
                geo.addPoint(vertex[0], vertex[1], vertex[2], lc_p, i + 1)

            gmsh.model.geo.synchronize()

            last_point = None
            edge_orientations = [None] * edges.__len__()

            for i, edge in enumerate(edges):
                try:
                    p1 = vertex_lookup[tuple(edge.Vertexes[0].Point)] + 1
                    p2 = vertex_lookup[tuple(edge.Vertexes[1].Point)] + 1
                    geo.addLine(p1, p2, i + 1)
                    if last_point is not None:
                        if p1 == last_point:
                            edge_orientations[i] = 1
                            last_point = p2
                        else:
                            edge_orientations[i] = -1
                            last_point = p1
                    else:
                        edge_orientations[i] = 1
                        last_point = p2
                except Exception as e:
                    logger.error(f'Error adding edge {edge}:\n{e}')
            gmsh.model.geo.synchronize()

            ids = (np.array(range(edges.__len__())) + 1) * np.array(edge_orientations)
            try:
                geo.addCurveLoop(ids, 1)
            except Exception as e:
                if e.args[0] == 'Curve loop 1 is wrong':
                    pass
                raise e
            gmsh.model.geo.synchronize()

            geo.addPlaneSurface([1], 1)
            gmsh.model.geo.synchronize()

            gmsh.option.setNumber("General.Terminal", 0)
            gmsh.option.setNumber("Mesh.MeshSizeMin", 1)
            gmsh.option.setNumber("Mesh.MeshSizeMax", lc)

            # Finally, while the default "Frontal-Delaunay" 2D meshing algorithm
            # (Mesh.Algorithm = 6) usually leads to the highest quality meshes, the
            # "Delaunay" algorithm (Mesh.Algorithm = 5) will handle complex mesh size fields
            # better - in particular size fields with large element size gradients:
            # gmsh.option.setNumber("Mesh.Algorithm", 5)

            # gmsh.option.setNumber("Mesh.Algorithm", 8)
            gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 2)
            gmsh.model.mesh.generate(2)
            gmsh.model.mesh.optimize('Relocate2D')

            # recombine to quad mesh
            # https://gitlab.onelab.info/gmsh/gmsh/-/issues/784
            gmsh.option.setNumber('General.Terminal', 0)
            # gmsh.model.mesh.setRecombine(2, 1)
            # gmsh.option.setNumber('SubdivisionAlgorithm ', 2)
            gmsh.model.mesh.recombine()
            # gmsh.model.mesh.recombine()
            mesh = extract_to_meshio()
            # mesh.write('/tmp/test.vtk')

        except Exception as e:
            logger.error(f'Error creating mesh for face {self.id}')
            gmsh.finalize()
            raise e

        gmsh.finalize()

        return mesh

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_inst': self.fc_inst.copy(),
                     'fc_obj_file': self.fc_obj_file,
                     'normal': self.normal}
        init_dict.update(kwargs)
        new_face = self.__class__(**init_dict)
        return new_face

    def _on_save_update(self):
        self.update_area()
        self.update_normal()
