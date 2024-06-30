import uuid
from typing import Optional, Union
from logging import getLogger
from PySimultan2.geometry.geometry_base import (GeometryModel, SimultanLayer, SimultanVertex, SimultanEdge, SimultanFace,
                                                SimultanVolume, SimultanEdgeLoop)
from PySimultan2 import FileInfo
from .fc_geometry import FreeCADGeometry
from ..utils.tools import import_feature

import FreeCAD
import Part as FCPart


logger = getLogger('pysimultan_freecad')


def get_fc_property_type(value):
    if isinstance(value, str):
        return "App::PropertyString"
    elif isinstance(value, int):
        return "App::PropertyInteger"
    elif isinstance(value, float):
        return "App::PropertyFloat"
    elif isinstance(value, bool):
        return "App::PropertyBool"
    if isinstance(value, list):
        if all(isinstance(v, int) for v in value):
            return "App::PropertyIntegerList"
        elif all(isinstance(v, float) for v in value):
            return "App::PropertyFloatList"
        elif all(isinstance(v, str) for v in value):
            return "App::PropertyStringList"
        elif all(isinstance(v, bool) for v in value):
            return "App::PropertyBoolList"
        elif all(isinstance(v, FreeCAD.Vector) for v in value):
            return "App::PropertyVectorList"
    elif isinstance(value, FileInfo):
        return "App::PropertyFile"
    elif isinstance(value, FreeCAD.Vector):
        return "App::PropertyVector"
    elif isinstance(value, FCPart.Shape):
        return "Part::PropertyPartShape"


def update_feature_property(feature: FCPart.Feature,
                            key: str,
                            value: Union[str, int, float, bool, list, FileInfo, FreeCAD.Vector, FCPart.Shape,
                            list[str], list[int], list[float], list[bool], list[FreeCAD.Vector]],
                            prop_name: Optional[str] = None,
                            ):
    if not hasattr(feature, key):
        if prop_name is None:
            prop_name = get_fc_property_type(value)
        feature.addProperty(prop_name, key, "PySimultan", key)
    setattr(feature, key, value)
    feature.Document.save()


class Feature(object):

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'Unnamed Feature')
        self.uuid = kwargs.get('uuid', str(uuid.uuid4()))
        self.fc_obj_file: Optional[FreeCADGeometry] = kwargs.get('fc_obj_file', None)
        self.fc_obj_file_id = kwargs.get('fc_obj_file_id', None)  # id of the FreeCAD object in the FreeCAD file

        feature_ids = self.get_feature_property('feature_ids', [])
        if self.uuid not in feature_ids:
            feature_ids.append(self.uuid)
            self.update_feature_property(key='feature_ids', value=feature_ids, prop_name="App::PropertyStringList")

    @property
    def shape(self) -> Optional[FCPart.Shape]:
        return self.fc_obj_file.features[self.fc_obj_file_id].Shape

    @property
    def type_id(self):
        return self.fc_obj_file.features[self.fc_obj_file_id].TypeId

    def to_simgeo(self,
                  geo_model: Optional[GeometryModel] = None,
                  scale: float = 1.0):

        if geo_model is None:
            geo_model = GeometryModel(name=f'Geo model {self.name}',
                                      data_model=self._data_model)

        feature = self.fc_obj_file.features[self.fc_obj_file_id]

        # create_new_layer

        logger.info(f'Creating new layer for {feature.Name} {feature.Label}')
        layer = SimultanLayer(name=f'{feature.Name} {feature.Label} Layer',
                              geometry_model=geo_model)

        try:
            logger.info(f'Importing feature {feature.Name} {feature.Label}')
            import_feature(feature=feature,
                           layer=layer,
                           scale=scale)
        except Exception as e:
            logger.error(f'Error importing feature {self}: {e}')

        return geo_model

    def update_feature_property(self,
                                key: str,
                                value: Union[str, int, float, bool, list, FileInfo, FreeCAD.Vector, FCPart.Shape,
                                list[str], list[int], list[float], list[bool], list[FreeCAD.Vector]],
                                prop_name: Optional[str] = None,
                                ):
        feature = self.fc_obj_file.features[self.fc_obj_file_id]
        update_feature_property(feature=feature,
                                key=key,
                                value=value,
                                prop_name=prop_name)

    def get_feature_property(self, key, alternative=None):
        feature = self.fc_obj_file.features[self.fc_obj_file_id]
        try:
            return getattr(feature, key)
        except AttributeError:
            return alternative

    def __repr__(self):
        return f'Feature {self.name}'
