import os
import numpy as np
import logging
from typing import Optional

from PySimultan2 import DataModel, FileInfo
from PySimultan2.geometry.geometry_base import GeometryModel
from pysimultan_freecad.src.pysimultan_freecad.mapping.mapper import mapper
from pysimultan_freecad.src.pysimultan_freecad.freecad.utils import import_fc_geometry

logger = logging.getLogger(__name__)

project_dir = os.environ.get('PROJECT_DIR', '/simultan_projects')
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

new_data_model = DataModel.create_new_project(project_path=os.path.join(project_dir, 'test_geometry_import.simultan'),
                                              user_name='admin',
                                              password='admin')


def import_geometry():

    file_info = FileInfo(file_path=os.path.join(project_dir, 'test_import.FCStd'))
    free_cad_geometry = mapper.create_sim_component(import_fc_geometry(file_info=file_info,
                                                                       data_model=new_data_model),
                                                    data_model=new_data_model)

    free_form_file_info = FileInfo(file_path=os.path.join(project_dir, 'test_import_freeform_surfaces.FCStd'))
    free_form_geometry = mapper.create_sim_component(import_fc_geometry(file_info=free_form_file_info,
                                                                        data_model=new_data_model),
                                                     data_model=new_data_model)

    new_data_model.save()
    new_data_model.cleanup()
    mapper.clear()


def load_geometry():
    data_model = DataModel(project_path=os.path.join(project_dir, 'test_geometry_import.simultan'),
                           user_name='admin',
                           password='admin')
    typed_data = mapper.get_typed_data(data_model)
    FreeCADGeometry = mapper.get_mapped_class('free_cad_geometry')
    geo_1 = FreeCADGeometry.cls_instances[0]
    geo_2 = FreeCADGeometry.cls_instances[1]

    def create_new_geometry(data_model: Optional[DataModel] = None,
                            name: str = 'Unnamed Geometry Model') -> GeometryModel:

        return GeometryModel(name=name,
                             data_model=data_model)

    new_geo_model = create_new_geometry(data_model=data_model,
                                        name='test_geometry')

    for key, value in geo_1.features.items():
        feature = geo_1.create_feature_component(feature_id=key)
        sim_feature = mapper.create_sim_component(feature, data_model=data_model)
        sim_feature.to_simgeo(new_geo_model)

    for key, value in geo_2.features.items():
        feature = geo_2.create_feature_component(feature_id=key)
        sim_feature = mapper.create_sim_component(feature, data_model=data_model)
        sim_feature.to_simgeo(new_geo_model)

    data_model.save()
    data_model.cleanup()


if __name__ == '__main__':
    import_geometry()
    load_geometry()
