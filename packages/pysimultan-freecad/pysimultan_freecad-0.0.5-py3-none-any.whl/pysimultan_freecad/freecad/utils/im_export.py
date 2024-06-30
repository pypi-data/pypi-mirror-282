import os
from typing import Optional
from nicegui import ui
from PySimultan2 import FileInfo, DataModel


import FreeCAD
import Part as FCPart


def import_fc_geometry(data_model: DataModel,
                       file_info: Optional[FileInfo] = None):

    from ..fc_geometry import FreeCADGeometry, Assembly

    free_cad_geometry = FreeCADGeometry(name='free_cad_geometry',
                                        data_model=data_model,
                                        geometry_file=file_info)
    return free_cad_geometry
