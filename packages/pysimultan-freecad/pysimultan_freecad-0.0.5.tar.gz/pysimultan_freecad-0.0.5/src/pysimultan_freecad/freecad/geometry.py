import re
import io
import os
import tempfile
import numpy as np

from .logger import logger
from .geometry_utils import (create_fc_vertex, create_fc_edge, create_fc_edge_loop, create_fc_face,
                             create_fc_volume, create_stl_file, save_volume_fcstd, create_face_stl_str)

from PySimultan2.geometry.geometry_base import (SimultanLayer, SimultanVertex, SimultanEdge, SimultanEdgeLoop,
                                                SimultanFace, SimultanVolume)
from SIMULTAN.Data.Geometry import (Layer, Vertex, Edge, PEdge, Face, Volume, EdgeLoop)
from .utils.obb import create_oriented_bounding_box_openfoam_order

import FreeCAD
import Part as FCPart
import MeshPart

App = FreeCAD


class ExtendedVertex(SimultanVertex):

    @classmethod
    def from_fc_inst(cls, fc_vertex, **kwargs):
        return cls(x=fc_vertex.X,
                   y=fc_vertex.Y,
                   z=fc_vertex.Z,
                   **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fc_inst = None

    @property
    def fc_inst(self):
        if self._fc_inst is None:
            self._fc_inst = create_fc_vertex(self)
        return self._fc_inst

    def __repr__(self):
        return f'Vertex {self.id}: ({self.x}, {self.y}, {self.z})'


class ExtendedEdge(SimultanEdge):

    @classmethod
    def from_fc_inst(cls, fc_edge, **kwargs):

        return cls(vertices=[ExtendedVertex.from_fc_inst(fc_edge.Vertexes[0],
                                                         layer=kwargs.get('layer', None),
                                                         geometry_model=kwargs.get('geometry_model')),
                             ExtendedVertex.from_fc_inst(fc_edge.Vertexes[1],
                                                         layer=kwargs.get('layer', None),
                                                         geometry_model=kwargs.get('geometry_model'))],
                   **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fc_inst = None
        self.type = kwargs.get('type', 'line')

    @property
    def fc_inst(self):
        if self._fc_inst is None:
            self._fc_inst = create_fc_edge(self)
        return self._fc_inst

    @property
    def length(self):
        return self.fc_inst.Length

    def __repr__(self):
        return f'Edge {self.id}: {self.vertices[0]} -> {self.vertices[1]}'


class ExtendedEdgeLoop(SimultanEdgeLoop):

    @classmethod
    def from_fc_inst(cls, fc_edge_loop, **kwargs):

        name = kwargs.get('name', 'Unnamed Edge Loop')
        edges = [ExtendedEdge.from_fc_inst(e,
                                           layer=kwargs.get('layer'),
                                           geometry_model=kwargs.get('geometry_model')
                                           ) for e in fc_edge_loop.Edges]

        return cls(name=name,
                   edges=edges,
                   **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._fc_inst = None

    @property
    def fc_inst(self):
        if self._fc_inst is None:
            self._fc_inst = create_fc_edge_loop(self)
        return self._fc_inst


class ExtendedFace(SimultanFace):

    @classmethod
    def from_fc_inst(cls, fc_face, **kwargs):

        name: str = kwargs.get('name', 'Unnamed Face')
        material = kwargs.get('material', None)

        return cls(name=name,
                   boundary=ExtendedEdgeLoop.from_fc_inst(fc_face.OuterWire,
                                                          layer=kwargs.get('layer'),
                                                          geometry_model=kwargs.get('geometry_model')
                                                          ),
                   material=material,
                   **kwargs)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self._fc_inst = None
        self._stl_str = None

        self._stl_file = None
        self.extruded = kwargs.get('extruded', False)

    @property
    def txt_id(self):
        return re.sub('\W+', '', 'a' + str(self.id))

    @property
    def fc_face(self):
        return self.fc_inst

    @property
    def fc_inst(self):
        if self._fc_inst is None:
            self._fc_inst = create_fc_face(self)
        return self._fc_inst

    @property
    def stl_str(self):
        if self._stl_str is None:
            self._stl_str = self.create_stl_str()
        return self._stl_str

    @property
    def vertices(self):
        return self.boundary.vertices

    def create_stl_str(self, of=False, scale_to_m=False):
        """

        :param of: Export for openFoam
        :param scale_to_m: scale stl export to m instead of mm
        :return: stl string
        """

        # logger.debug(f'creating stl string for face {self.id}...')

        return create_face_stl_str(self,
                                   of=of,
                                   scale_to_m=scale_to_m,
                                   linear_deflection=self.surface_mesh_parameters.linear_deflection,
                                   angular_deflection=self.surface_mesh_parameters.angular_deflection)

    def create_mesh(self, max_length=99999999):
        mesh_shp = MeshPart.meshFromShape(Shape=self.fc_inst,
                                          MaxLength=max_length)
        return mesh_shp

    def get_normal(self, point):
        uv = self.fc_inst.Surface.parameter(point)
        nv = self.fc_inst.normalAt(*uv)
        return nv.normalize()

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_face': self.fc_face.copy()}
        init_dict.update(kwargs)
        new_face = Face(**init_dict)
        return new_face


class ExtendedVolume(SimultanVolume):

    def __init__(self, *args, **kwargs):

        self._obb = None

        super().__init__(*args, **kwargs)
        self._fc_inst = None
        self.base_block_mesh = kwargs.get('base_block_mesh', None)
        self.obb = kwargs.get('obb', None)

        self.material = kwargs.get('material')

    @property
    def txt_id(self):
        return re.sub('\W+', '', 'a' + str(self.id))

    @property
    def fc_inst(self):
        if self._fc_inst is None:
            self._fc_inst = create_fc_volume(self)
        return self._fc_inst

    @property
    def obb(self) -> np.ndarray:
        if self._obb is None:
            self._obb = self.create_obb()
        return self._obb

    @obb.setter
    def obb(self, value):
        self._obb = value

    @property
    def stl(self):
        return ''.join([x.stl for x in self.faces])

    def create_obb(self, scale=1.01) -> np.ndarray:
        corner_vertices = create_oriented_bounding_box_openfoam_order(
            np.array([(x.X, x.Y, x.Z) for x in self.fc_inst.Shape.Vertexes])).round(6)
        center = np.mean(corner_vertices, axis=0)
        vecs = corner_vertices - center
        unit_vecs = vecs / np.linalg.norm(vecs, axis=0)
        scaled_points = corner_vertices + unit_vecs * scale
        return scaled_points

    # def create_base_block_mesh(self) -> BlockMeshCase:
    #    return BlockMeshCase.from_volume(self)

    # def create_snappy_hex_mesh_case(self, name='Unnamed SnappyHexMeshCase') -> SnappyHexMeshCase:
    #     return SnappyHexMeshCase.from_volume(self, name=name)

    def save_fcstd(self, filename, shape_type='solid'):
        """
        save as freecad document
        :param filename: full filename; example: '/tmp/test.FCStd'
        :param shape_type: 'solid', 'faces'
        """
        doc = App.newDocument(f"SolidMaterial {self.name}")
        if shape_type == 'solid':
            __o__ = doc.addObject("Part::Feature", f'SolidMaterial {self.name} {self.id}')
            __o__.Shape = self._fc_inst.Shape
        elif shape_type == 'face':
            for face in self.faces:
                __o__ = doc.addObject("Part::Face", f'Face {face.name} {face.id}')
                __o__.Shape = face.fc_solid.Shape
        doc.recompute()
        doc.saveCopy(filename)

    def export_stl(self, filename):
        try:
            logger.debug(f'exporting .stl for solid {self.id}')
            new_file = open(filename, 'w')
            new_file.writelines(self.stl)
            new_file.close()
            logger.debug(f'    finished exporting .stl for solid {self.id}')
        except Exception as e:
            logger.error(f'error while exporting .stl for solid {self.id}: {e}')

    def export_step(self, filename):
        logger.debug(f'exporting .stp for solid {self.id}')

        path = os.path.dirname(filename)
        os.makedirs(path, exist_ok=True)

        try:
            from .tools import name_step_faces

            __objs__ = [self._fc_inst]

            fd, tmp_file = tempfile.mkstemp(suffix='.stp')
            os.close(fd)

            FCPart.export(__objs__, tmp_file)
            names = [f'Face {f.name} {f.id}' for f in self.faces]
            names_dict = {k: v for k, v in zip(range(names.__len__()), names)}
            name_step_faces(fname=tmp_file, name=names_dict, new_fname=filename)
        except Exception as e:
            logger.error(f'error while exporting .stp for solid {self.id}:\n{e}')
        finally:
            try:
                os.remove(tmp_file)
            except FileNotFoundError as e:
                pass

        logger.debug(f'    finished exporting .stp for solid {self.id}')
