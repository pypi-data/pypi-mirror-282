from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from .base_fc_geometry import BaseFCGeometry

import FreeCAD
import Part as FCPart


class Vertex(BaseFCGeometry):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fc_vertex = kwargs.get('fc_vertex', kwargs.get('fc_inst', kwargs.get('_fc_inst', None)))

    @property
    def fc_vertex(self) -> Union[FCPart.Shape, None]:
        return self.fc_inst

    @fc_vertex.setter
    def fc_vertex(self, value: Union[FCPart.Face, FCPart.Shape]):
        self.fc_inst = value

    @property
    def _fc_vertex(self) -> Union[FCPart.Shape, None]:
        return self._fc_inst

    @_fc_vertex.setter
    def _fc_vertex(self, value: Union[FCPart.Face, FCPart.Shape]) -> None:
        self._fc_edge = value

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_inst': self.fc_inst.copy(),
                     'fc_obj_file': self.fc_obj_file}
        init_dict.update(kwargs)
        new_obj = self.__class__(**init_dict)
        return new_obj
