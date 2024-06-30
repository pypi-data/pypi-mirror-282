from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
import os
import uuid
import tempfile
import re
from ..logger import logger
from .fc_geometry import save_obj, load_obj

from SIMULTAN.Data import SimId

import FreeCAD
import Part as FCPart


if TYPE_CHECKING:
    from .fc_geometry import FreeCADGeometry


class BaseFCGeometry(object):

    def __init__(self, *args, **kwargs):

        self._fc_feature = None

        self._fc_inst = None
        self.uuid = kwargs.get('uuid', str(uuid.uuid4()))
        self._txt_id = None
        self.name = kwargs.get('name', None)
        self.fc_obj_file: Optional[FreeCADGeometry] = kwargs.get('fc_obj_file', None)
        self.fc_obj_file_id = kwargs.get('fc_obj_file_id', None)         # id of the FreeCAD object in the FreeCAD file
        self.fc_inst = kwargs.get('fc_inst', kwargs.get('_fc_inst', None))
        self._vertices = kwargs.get('_vertices', [])

    def __load_init__(self, *args, **kwargs):
        self._fc_inst = None
        self._feature = None
        self._fc_feature = None

    def _on_save_update(self):
        pass

    @property
    def fc_inst(self) -> Union[FCPart.Shape, None]:
        try:
            if self._fc_inst is None and self.fc_obj_file is not None:
                self._fc_feature = load_obj(self,
                                            freecad_geometry=self.fc_obj_file)
                self._fc_inst = self._fc_feature.Shape
        except Exception as e:
            logger.error(f'error while loading FreeCAD object from file for {self.id}:\n{e}')
            raise e
        return self._fc_inst

    @fc_inst.setter
    def fc_inst(self, value: Union[FCPart.Shape]) -> None:

        if value is None:
            self._fc_inst = None
            return
        if not isinstance(value, FCPart.Shape):
            self._fc_inst = FCPart.Shape(value)
        else:
            self._fc_inst = value

        self._fc_inst = value
        if value is not None and self.txt_id is not None:
            fc_id, __o__ = save_obj(self,
                                    freecad_geometry=self.fc_obj_file)
            self.fc_obj_file_id = fc_id
            self._fc_feature = __o__
            self._on_save_update()

    @property
    def txt_id(self) -> str:
        if self._txt_id is None:
            if hasattr(self, 'uuid'):
                self._txt_id = re.sub('\W+','', 'a' + str(self.uuid))
            elif hasattr(self, 'id'):
                if isinstance(self.id, uuid.UUID):
                    self._txt_id = re.sub('\W+','', 'a' + str(self.id))
                elif isinstance(self.id, SimId):
                    self._txt_id = f'f{str(self.id.GlobalId)}_{str(self.id.LocalId)}'.replace('-', '_')
            else:
                return None
        return self._txt_id

    @txt_id.setter
    def txt_id(self, value):
        self._txt_id = value

    @property
    def vertices(self):
        from .vertex import Vertex
        self.fc_inst.Vertexes

    def export_step(self, filename):

        logger.debug(f'exporting .step for face {self.id}...')

        try:
            from ..tools import name_step_faces

            doc = FreeCAD.newDocument()

            fd, tmp_file = tempfile.mkstemp(suffix='.stp')
            os.close(fd)

            __o__ = doc.addObject("Part::Feature", f'{str(self.id)}')
            __o__.Label = f'{str(self.id)}'
            __o__.Shape = self.fc_inst

            FCPart.export(doc.Objects, tmp_file)

            # rename_faces:
            names = [str(self.id)]
            names_dict = {k: v for k, v in zip(range(names.__len__()), names)}
            name_step_faces(fname=tmp_file, name=names_dict, new_fname=filename)

            logger.debug(f'    finished .step export for face {self.id}')

        except Exception as e:
            logger.error(f'error while exporting .stp for face {self.id}:\n{e}')
        finally:
            try:
                os.remove(tmp_file)
            except FileNotFoundError as e:
                pass

    def __repr__(self):
        rep = f'Face {self.name} {self.txt_id}'
        return rep

    def __hash__(self):
        return id(self)

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_inst': self.fc_inst.copy(),
                     'fc_obj_file': self.fc_obj_file}
        init_dict.update(kwargs)
        new_face = self.__class__(**init_dict)
        return new_face
