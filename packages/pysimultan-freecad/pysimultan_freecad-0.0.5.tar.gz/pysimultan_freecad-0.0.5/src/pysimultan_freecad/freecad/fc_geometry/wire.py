from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from .base_fc_geometry import BaseFCGeometry

import FreeCAD
import Part as FCPart
import MeshPart


class Wire(BaseFCGeometry):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self._length = kwargs.get('_length', None)
        self._is_closed = kwargs.get('_is_closed', None)
        self.fc_wire = kwargs.get('fc_wire', None)

    @property
    def fc_wire(self) -> Union[FCPart.Shape, None]:
        return self.fc_inst

    @fc_wire.setter
    def fc_wire(self, value: Union[FCPart.Wire, FCPart.Shape]):
        self.fc_inst = value

    @property
    def _fc_wire(self) -> Union[FCPart.Shape, None]:
        return self._fc_inst

    @_fc_wire.setter
    def _fc_wire(self, value: Union[FCPart.Wire, FCPart.Shape]) -> None:
        self._fc_wire = value

    @property
    def length(self) -> float:
        self._length = self.fc_inst.Length
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        self._length = value

    @property
    def is_closed(self) -> bool:
        self._is_closed = self.fc_inst.isClosed()
        return self._is_closed

    @is_closed.setter
    def is_closed(self, value: bool) -> None:
        self._is_closed = value

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_inst': self.fc_inst.copy(),
                     'fc_obj_file': self.fc_obj_file}
        init_dict.update(kwargs)
        new_obj = self.__class__(**init_dict)
        return new_obj

    def update_length(self):
        self._length = self.fc_inst.Length

    def update_is_closed(self):
        self._is_closed = self.fc_inst.isClosed()

    def _on_save_update(self):
        self.update_length()
        self.update_is_closed()
