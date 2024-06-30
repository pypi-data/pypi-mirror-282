import os
import re
import uuid
import itertools
from typing import Optional, Union, Tuple
from PySimultan2.files import FileInfo

from ..utils.geometry import export_objects

import FreeCAD
import Part as FCPart

from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    pass


export_iter = itertools.count()


def save_obj(obj,
             file_name: str = None,
             freecad_geometry: Optional['FreeCADGeometry'] = None) -> Optional[tuple[int, FCPart.Feature]]:

    if file_name is not None:
        if obj.fc_inst is not None:
            if os.path.exists(file_name):
                os.remove(file_name)

            export_objects(obj.fc_inst, file_name, add_suffix=False)
    else:
        if obj.fc_inst is not None:
            if hasattr(obj, '_wrapped_obj'):
                sim_id = f'{obj._wrapped_obj.Id.GlobalId}_{obj._wrapped_obj.Id.LocalId}'
            else:
                sim_id = ''
            fc_id, __o__ = freecad_geometry.add_object(obj.fc_inst,
                                                       obj_id=obj.txt_id,
                                                       sim_id=sim_id,
                                                       name=obj.name if obj.name is not None else obj.txt_id)
            freecad_geometry.save()
            return fc_id, __o__
        else:
            raise ValueError('No FreeCAD object to save')


def load_obj(geo_obj,
             file_info: Optional[FileInfo] = None,
             freecad_geometry: Optional['FreeCADGeometry'] = None) -> Optional[FCPart.Shape]:

    if file_info is None:
        loaded_geo_obj = freecad_geometry.get_object_by_id(geo_obj.txt_id)
        return loaded_geo_obj
        # if loaded_geo_obj is not None:
        #     return FCPart.Shape(loaded_geo_obj.Shape)
        # else:
        #     return None
    else:
        file_name = file_info.file_path
        if not os.path.isfile(file_name):
            return None
        doc = FreeCAD.open(file_name)
        return doc.Objects[0]


class classproperty(object):

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        return self.getter(owner)


class FreeCADGeometry(object):

    def __init__(self, *args, **kwargs):

        self.uuid = kwargs.get('uuid', str(uuid.uuid4()))

        self.name = kwargs.get('name', 'Unnamed FreeCAD Geometry Object')
        self.geometry_file: Optional[FileInfo] = kwargs.get('geometry_file', None)

        if self.geometry_file is not None:
            self.doc = FreeCAD.open(self.geometry_file.file_path)
        else:
            self.doc = FreeCAD.newDocument()
            self.doc.FileName = f"{self.txt_id}.FCStd"
            self.doc.save()
            self.geometry_file = FileInfo(file_path=self.doc.FileName)
            self.doc = FreeCAD.open(self.geometry_file.file_path)

        self._lookup_dict = {}

    def __load_init__(self, *args, **kwargs):
        self._lookup_dict = {}
        if self.geometry_file is not None:
            self.doc = FreeCAD.open(self.geometry_file.file_path)
        else:
            self.doc = FreeCAD.newDocument()
            self.doc.FileName = f"{self.txt_id}.FCStd"
            self.doc.save()
            self.geometry_file = FileInfo(file_path=self.doc.FileName)
            self.doc = FreeCAD.open(self.geometry_file.file_path)

    @property
    def txt_id(self):
        return re.sub(r'\W+', '', 'a' + str(self.uuid))

    @property
    def lookup_dict(self):
        if not self._lookup_dict:
            self._lookup_dict = {obj.Label: obj for obj in self.doc.Objects}
        return self._lookup_dict

    @property
    def vertices(self):
        return [x for x in self.doc.Objects if isinstance(x, FCPart.Vertex)]

    @property
    def edges(self):
        return [x for x in self.doc.Objects if isinstance(x, FCPart.Edge)]

    @property
    def wires(self):
        return [x for x in self.doc.Objects if isinstance(x, FCPart.Wire)]

    @property
    def faces(self):
        return [x for x in self.doc.Objects if isinstance(x, FCPart.Face)]

    @property
    def solids(self):
        return [x for x in self.doc.Objects if isinstance(x, FCPart.Solid)]

    @property
    def features(self) -> dict[str, FCPart.Feature]:
        return {x.ID: x for x in self.doc.Objects if isinstance(x, FCPart.Feature)}

    def add_object(self,
                   obj: Union[FCPart.Shape, FCPart.Feature],
                   obj_id: str,
                   sim_id: str = '',
                   name: str = '',
                   fc_properties: Optional[dict[str, Tuple[str, Any]]] = None,
                   ) -> tuple[int, FCPart.Feature]:

        if obj_id in self.lookup_dict:
            __o__ = self.lookup_dict[obj_id]
        else:
            __o__ = self.doc.addObject("Part::Feature", name)

        if not hasattr(__o__, 'PySimComponentIDs'):
            __o__.addProperty("App::PropertyStringList", "PySimComponentIDs", "SIMULTAN", "IDs of the components")
        if sim_id not in __o__.PySimComponentIDs:
            __o__.PySimComponentIDs = [*__o__.PySimComponentIDs, sim_id]

        for key, value in fc_properties:
            if not hasattr(__o__, key):
                __o__.addProperty(key, value(0), "PySimultan", value(1))
            setattr(__o__, key, value)

        __o__.Label = obj_id
        __o__.Label2 = name

        if isinstance(obj, FCPart.Shape):
            __o__.Shape = obj
        elif isinstance(obj, FCPart.Feature):
            __o__.Shape = obj.Shape
        else:
            raise ValueError(f'Unsupported object type: {type(obj)}')

        self._lookup_dict[obj_id] = __o__
        self.save()
        return __o__.ID, __o__

    def remove_object(self, obj_id):
        obj = self.lookup_dict.get(obj_id, None)
        if obj is not None:
            self.doc.removeObject(obj.Name)
            self._lookup_dict.pop(obj_id, None)

    def get_object_by_id(self, obj_id: str):
        """
        Get object by ID which is the Label of the object (doc.Objects.Label). This is usually the txt_id of the object.
        :param obj_id:
        :return:
        """

        obj = self.lookup_dict.get(obj_id, None)
        if obj is None:
            self._lookup_dict = {obj.Label: obj for obj in self.doc.Objects}
            obj = self.lookup_dict.get(obj_id, None)
        return obj

    def get_object_by_geo_id(self, geo_id: int):
        """
        Get object by ID which is the ID of the object (doc.Objects.ID).
        :param geo_id:
        :return:
        """
        obj = next((x for x in self.doc.Objects if x.ID == geo_id), None)
        return obj

    def save(self):
        self.doc.recompute()
        self.doc.save()

    def create_feature_component(self, feature_id):
        feature = self.features.get(feature_id, None)
        if feature is None:
            raise ValueError(f'Feature ID {feature_id} not found')

        from .feature import Feature

        return Feature(name=f'{feature.Label} ({feature.ID})',
                       fc_obj_file=self,
                       fc_obj_file_id=feature_id)
