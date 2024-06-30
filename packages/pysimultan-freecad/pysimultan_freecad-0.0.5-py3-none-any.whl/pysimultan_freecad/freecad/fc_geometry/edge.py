from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Union
from .base_fc_geometry import BaseFCGeometry

import FreeCAD
import Part as FCPart

from .vertex import Vertex


class Edge(BaseFCGeometry):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self._vertices = None
        self._length = kwargs.get('_length', None)
        self.fc_edge = kwargs.get('fc_edge', kwargs.get('fc_inst', kwargs.get('_fc_inst', None)))
        self.vertices = kwargs.get('vertices', None)

    @property
    def fc_edge(self) -> Union[FCPart.Shape, None]:
        return self.fc_inst

    @fc_edge.setter
    def fc_edge(self, value: Union[FCPart.Face, FCPart.Shape]):
        self.fc_inst = value

    @property
    def _fc_edge(self) -> Union[FCPart.Shape, None]:
        return self._fc_inst

    @_fc_edge.setter
    def _fc_edge(self, value: Union[FCPart.Face, FCPart.Shape]) -> None:
        self._fc_edge = value

    @property
    def length(self) -> float:
        self._length = self.fc_inst.Length
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        self._length = value

    @property
    def vertices(self) -> list[Vertex]:
        if self._vertices is None:
            self._vertices = [Vertex(fc_vertex=vertex,
                                     fc_obj_file=self.fc_obj_file,
                                     data_model=self._data_model) for vertex in self.fc_inst.Vertexes]

        return self._vertices

    @vertices.setter
    def vertices(self, value: list[Union[Vertex, FCPart.Vertex]]) -> None:
        if value is None:
            self._vertices = value
            return

        if isinstance(value[0], Vertex):
            v_0 = value[0].fc_vertex
        elif isinstance(value[0], FCPart.Vertex):
            v_0 = value[0]

        if isinstance(value[1], Vertex):
            v_1 = value[1].fc_vertex
        elif isinstance(value[1], FCPart.Vertex):
            v_1 = value[1]

        self.fc_inst = FCPart.Edge(v_0, v_1)
        self._vertices = value

    def _on_save_update(self):
        self.update_length()

    def copy(self, *args, **kwargs):
        init_dict = {'name': f'Copy of {self.name}',
                     'fc_inst': self.fc_inst.copy(),
                     'fc_obj_file': self.fc_obj_file}
        init_dict.update(kwargs)
        new_obj = self.__class__(**init_dict)
        return new_obj

    def update_length(self):
        self.length = self.fc_inst.Length
