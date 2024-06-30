import os
from typing import List, Union, Optional, TYPE_CHECKING, Literal, Any
import tempfile
import numpy as np

from .face import Face
from random import random

from .base_fc_geometry import BaseFCGeometry
from ..logger import logger

import FreeCAD
import Part as FCPart
from FreeCAD import Base


App = FreeCAD


class Solid(BaseFCGeometry):

    def __init__(self, *args, **kwargs):
        super(Solid, self).__init__(*args, **kwargs)

        self._mesh = None
        self._volume = kwargs.get('volume', None)
        self._is_closed = kwargs.get('is_closed', None)

        self.type = kwargs.get('type', None)
        self.features: dict[str: Optional[Face, Solid]] = kwargs.get('features', {})

    def __load_init__(self, *args, **kwargs):
        super(Solid, self).__load_init__(*args, **kwargs)
        self._mesh = kwargs.get('_mesh', None)

    @property
    def faces(self):
        if self._faces is None:
            if self.fc_inst is not None:
                self._faces = [Face(fc_face=x,
                                    fc_obj_file=self.fc_obj_file) for x in self.fc_inst.Faces]
            else:
                return []
        return self._faces

    @faces.setter
    def faces(self, value: List['Face']):
        shell = FCPart.makeShell(value)
        shell.sewShape()
        shell.fix(1e-7, 1e-7, 1e-7)
        self.fc_inst = FCPart.Solid(shell)

    @property
    def fc_solid(self):
        return self.fc_inst

    @fc_solid.setter
    def fc_solid(self, value):
        self.fc_inst = value

    @property
    def volume(self) -> float:
        if self._volume is None:
            self._volume = self.fc_inst.Volume
        return self._volume

    @property
    def stl(self):
        return ''.join([x.stl for x in self.faces])

    @property
    def face_names(self):
        return [str(x.txt_id) for x in self.faces]

    @property
    def is_closed(self):
        self._is_closed = self.fc_inst.isClosed()
        return self._is_closed

    @is_closed.setter
    def is_closed(self, value: bool):
        self._is_closed = value

    def generate_faces(self):
        self._faces = [Face(fc_face=x,
                            fc_obj_file=self.fc_obj_file) for x in self.fc_inst.Faces]
        return self._faces

    def calculate_volume(self):
        self._volume = self.fc_inst.Volume
        return self._volume

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
            from ..tools import name_step_faces

            __objs__ = [self.fc_inst]

            fd, tmp_file = tempfile.mkstemp(suffix='.stp')
            os.close(fd)

            FCPart.export(__objs__, tmp_file)
            names = self.face_names
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

    def get_location_in_mesh(self):

        vec0 = self.fc_inst.Shape.CenterOfMass
        vec = vec0

        while not self.fc_inst.Shape.isInside(vec, 0, True):
            vec = Base.Vector(random() * (self.fc_inst.Shape.BoundBox.XMax - self.fc_inst.Shape.BoundBox.XMin) + self.fc_inst.Shape.BoundBox.XMin,
                              random() * (self.fc_inst.Shape.BoundBox.YMax - self.fc_inst.Shape.BoundBox.YMin) + self.fc_inst.Shape.BoundBox.YMin,
                              random() * (self.fc_inst.Shape.BoundBox.ZMax - self.fc_inst.Shape.BoundBox.ZMin) + self.fc_inst.Shape.BoundBox.ZMin)

        return np.array(vec)

    def generate_solid_from_faces(self):

        if not self.faces:
            return None

        logger.info(f'Generating solid from faces: {self.name} {self.txt_id}')

        faces = []
        try:
            [faces.extend(x.fc_face.Faces) for x in self.faces]
            shell = FCPart.makeShell(faces)
            shell.sewShape()
            shell.fix(1e-7, 1e-7, 1e-7)
            solid = FCPart.Solid(shell)
        except Exception as e:
            logger.error(f'Error while generating solid from faces: {self}\n{e}')
            raise e

        if not solid.isClosed():
            logger.error(f'SolidMaterial {self.id}: solid is not closed')

        doc = App.newDocument()
        __o__ = doc.addObject("Part::Feature", f'{str(self.txt_id)}')
        __o__.Label = f'{str(self.txt_id)}'
        __o__.Shape = solid

        logger.debug(f'Successfully finished generation of solid from faces: {self.txt_id}')

        return __o__

    def save_fcstd(self, filename, shape_type='solid'):
        """
        save as freecad document
        :param filename: full filename; example: '/tmp/test.FCStd'
        :param shape_type: 'solid', 'faces'
        """
        doc = App.newDocument(f"SolidMaterial {self.name}")
        if shape_type == 'solid':
            __o__ = doc.addObject("Part::Feature", f'SolidMaterial {self.name} {self.id}')
            __o__.Shape = self.fc_inst.Shape
        elif shape_type == 'face':
            for face in self.faces:
                __o__ = doc.addObject("Part::Face", f'Face {face.name} {face.id}')
                __o__.Shape = face.fc_inst.Shape
        doc.recompute()
        doc.saveCopy(filename)

    def is_inside(self, vec: Base.Vector):
        return self.fc_inst.Shape.isInside(vec, 0, True)

    def create_block_mesh(self):
        raise NotImplementedError('create_block_mesh is not implemented yet')

    def common(self, other):
        """
        Find common with other solid
        :param other:
        :return: common faces
        """

        return self.fc_inst.Shape.Shells[0].common(other.fc_inst.Shape.Shells[0])

    def save(self):
        if self.fc_obj_file is not None:
            self.fc_obj_file.save()
        self._data_model.save()

    def __repr__(self):
        rep = f'SolidMaterial {self.name} {self.Volume}'
        return rep

    def update_is_closed(self):
        self._is_closed = self.fc_inst.isClosed()
        return self._is_closed

    def _on_save_update(self):
        self.calculate_volume()
        self.update_is_closed()
