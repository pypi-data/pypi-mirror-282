import uuid
import re
from .base_fc_geometry import BaseFCGeometry
from SIMULTAN.Data import SimId
from .fc_geometry import FreeCADGeometry

import FreeCAD
import Part as FCPart

from typing import TYPE_CHECKING, Optional, Union
if TYPE_CHECKING:
    from .base_fc_geometry import BaseFCGeometry


class Assembly(object):

    def __init__(self, *args, **kwargs):

        self._features = kwargs.get('_features', {})
        self._interfaces = []

        self.uuid = kwargs.get('uuid', str(uuid.uuid4()))
        self._txt_id = None
        self.name = kwargs.get('name', None)
        self.fc_obj_file: Optional[FreeCADGeometry] = kwargs.get('fc_obj_file', None)
        if self.fc_obj_file is None:
            self.fc_obj_file = FreeCADGeometry(name=self.txt_id,
                                               data_model=kwargs.get('data_model', None))

        self.fc_inst = kwargs.get('fc_inst', kwargs.get('fc_face', None))
        self.interfaces = kwargs.get('interfaces', [])
        self.comp_solid = kwargs.get('comp_solid', None)

    def add_interface(self,
                      interface: Union[FCPart.Shape, FCPart.Feature, BaseFCGeometry],
                      obj_id: str = None,
                      name: str = None):

        self._interfaces.append(self.add_geometry(interface,
                                                  obj_id=obj_id,
                                                  name=name))

    def add_feature(self,
                    feature: str,
                    geometry: Union[FCPart.Shape, FCPart.Feature, BaseFCGeometry],
                    obj_id: str = None,
                    name: str = None):

        if isinstance(geometry, (FCPart.Shape, FCPart.Feature)):
            # create geometry object
            from . import Face, Solid, Edge, Assembly

            if isinstance(geometry, FCPart.Face):
                geometry = Face(fc_inst=geometry,
                                fc_obj_file=self.fc_obj_file,
                                name=name)
            elif isinstance(geometry, FCPart.Solid):
                geometry = Solid(fc_inst=geometry,
                                 fc_obj_file=self.fc_obj_file,
                                 name=name)

        fc_id = self.add_geometry(geometry,
                                  obj_id=obj_id,
                                  name=name)

        self._features[feature] = geometry
        return fc_id

    def get_feature(self, feature: str):
        return self.fc_obj_file.get_object_by_geo_id(self._features[feature])

    @property
    def features(self):
        return self._features

    def add_geometry(self,
                     geometry: Union[FCPart.Shape, FCPart.Feature, BaseFCGeometry],
                     obj_id: str = None,
                     name: str = None):

        if isinstance(geometry, (FCPart.Shape, FCPart.Feature)):
            fc_id, __0__ = self.fc_obj_file.add_object(geometry,
                                                       obj_id=obj_id,
                                                       name=name)

        elif isinstance(geometry, BaseFCGeometry):
            fc_id, __0__ = self.fc_obj_file.add_object(geometry.fc_inst,
                                                       obj_id=geometry.txt_id,
                                                       name=geometry.name if geometry.name is not None else geometry.txt_id)
        else:
            raise ValueError('Geometry type not supported')

        self.fc_obj_file.save()
        return fc_id

    @property
    def txt_id(self) -> str:
        if self._txt_id is None:
            if hasattr(self, 'uuid'):
                self._txt_id = re.sub('\W+', '', 'a' + str(self.uuid))
            elif hasattr(self, 'id'):
                if isinstance(self.id, uuid.UUID):
                    self._txt_id = re.sub('\W+', '', 'a' + str(self.id))
                elif isinstance(self.id, SimId):
                    self._txt_id = f'f{str(self.id.GlobalId)}_{str(self.id.LocalId)}'.replace('-', '_')
            else:
                return None
        return self._txt_id

    @txt_id.setter
    def txt_id(self, value):
        self._txt_id = value

    @property
    def fc_features(self):
        return self.fc_obj_file.features

    def generate_comp_solid(self):
        from .solid import Solid
        comp_solid_shape = FCPart.CompSolid([x for x in self.fc_obj_file.solids])
        self.comp_solid = Solid(fc_inst=comp_solid_shape,
                                fc_obj_file=FreeCADGeometry(name=self.txt_id),
                                name=self.txt_id + '_comp_solid')
        return self.comp_solid
