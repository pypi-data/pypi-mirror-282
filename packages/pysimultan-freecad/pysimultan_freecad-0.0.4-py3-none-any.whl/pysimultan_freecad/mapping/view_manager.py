from typing import List
from nicegui import ui, events
from SIMULTAN.Data import SimId
from asyncio import sleep
import numpy as np

from typing import Optional, TYPE_CHECKING

from ..freecad.logger import logger

from PySimultan2.geometry import GeometryModel

from nicegui.elements.scene_object3d import Object3D
from PySimultanUI.src.pysimultanui import ViewManager
from PySimultanUI.src.pysimultanui.views.component_detail_base_view import ComponentDetailBaseView
from PySimultanUI.src.pysimultanui.views.detail_views import show_detail
from PySimultanUI.src.pysimultanui.geometry_3d.scene import ExtendedScene
from PySimultanUI.src.pysimultanui.geometry_3d.three_views import (display_vertices, display_edges, display_wire,
                                                                   display_face, display_solid)

from PySimultanUI.src.pysimultanui.geometry_3d.tools import display_feature

from PySimultanUI.src.pysimultanui.geometry_3d.objects3d import Wire, Mesh, Spline

import FreeCAD
import Part as FCPart

view_manager = ViewManager()


def rgb_to_hex(rgb: List[int]) -> str:
    if rgb is None:
        return '#000000'
    return f'#{rgb[0] << 16 | rgb[1] << 8 | rgb[2]:06x}'


def get_feature_color(feature: FCPart.Feature,
                      hex_color: bool = False):
    rgba_string = feature.ShapeMaterial.Properties['AmbientColor']
    rgba_values = rgba_string.strip('()').split(',')
    rgb = [int(float(value.strip()) * 255) for value in rgba_values[:3]]

    if hex_color:
        return rgb_to_hex(rgb)
    else:
        return rgb


class FCGeometryDetailView(ComponentDetailBaseView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scene = None
        self.objects_3d: dict[int: Object3D] = {}

        self.selected = set()
        self.multi_select = False

    @ui.refreshable
    def ui_content(self, *args, **kwargs):
        super().ui_content(*args, **kwargs)

        with ui.row():
            ui.label('Geometry File: ')
            ui.label(self.component.geometry_file.name)

        self.three_d_view()
        self.features_list()

    @ui.refreshable
    def three_d_view(self):
        with ExtendedScene(on_click=self.handle_click,
                           background_color='#222').classes('w-full') as self.scene:

            scene = self.scene

            x_height = 0
            y_height = 0
            z_height = 0

            for feature in self.component.features.values():

                group, (x_height_i, y_height_i, z_height_i) = display_feature(feature, scene)

                if x_height_i > x_height:
                    x_height = x_height_i
                if y_height_i > y_height:
                    y_height = y_height_i
                if z_height_i > z_height:
                    z_height = z_height_i

                self.objects_3d[feature.ID] = group

            scene.move_camera(x=x_height, y=-y_height, z=z_height * 2, duration=2)

    def select(self, feature_id: int):
        if feature_id in self.objects_3d:
            self.objects_3d[feature_id].material('#FF5733')
            self.scene.update()
            self.selected.add(feature_id)

    def deselect(self, feature_id: int):
        if feature_id in self.objects_3d:
            self.objects_3d[feature_id].material(get_feature_color(self.component.features[feature_id],
                                                                   hex_color=True)
                                                 )
            self.scene.update()
            self.selected.remove(feature_id)

    def handle_click(self, e: events.SceneClickEventArguments, *args, **kwargs):
        if e.hits:
            hit = e.hits[0]
            name = hit.object_name or hit.object_id

            if int(name) in self.selected:
                self.deselect(int(name))
            else:
                self.select(int(name))
            ui.notify(f'You clicked on feature {name} at ({hit.x:.2f}, {hit.y:.2f}, {hit.z:.2f})')
        else:
            for key in self.selected:
                self.deselect(key)

    def features_list(self):
        columns = [{'name': 'id', 'label': 'ID', 'field': 'id', 'sortable': True},
                   {'name': 'name', 'label': 'Name', 'field': 'name', 'sortable': True},
                   {'name': 'type', 'label': 'Type', 'field': 'type', 'sortable': True},
                   {'name': 'component', 'label': 'Component', 'field': 'component', 'sortable': False}
                   ]

        rows = []

        Feature = self.user.mapper.get_mapped_class('feature')

        for feature in self.component.features.values():
            components = []
            if hasattr(feature, 'feature_ids'):
                for feature_id in feature.feature_ids:
                    comp = next((x for x in Feature.cls_instances if x.uuid == feature_id), None)
                    if comp is not None:
                        components.append(comp.name)

            rows.append({'id': feature.ID,
                         'name': f'{feature.Label} ({feature.ID})',
                         'type': feature.TypeId,
                         'component': str(components)})

        asset_table = ui.table(columns=columns,
                               rows=rows,
                               title='Features',
                               row_key='id').classes('w-full bordered text-sm')

        asset_table.add_slot('body', r'''
                    <q-tr :props="props">
                        <q-td v-for="col in props.cols" :key="col.name" :props="props">
                            {{ col.value }}
                        </q-td>
                        <q-td auto-width>
                            <q-btn size="sm" color="blue" round dense
                                   @click="$parent.$emit('create_component', props)"
                                   icon="auto_fix_high" />
                            <q-btn size="sm" color="blue" round dense
                                   @click="$parent.$emit('detail', props)"
                                   icon="launch" />
                        </q-td>
                    </q-tr>
                ''')
        asset_table.on('create_component', self.create_feature_component)
        asset_table.on('detail', self.show_feature_component_detail)

    def create_feature_component(self, props):
        feature_id = props.args['key']
        # feature = self.component.features[feature_id]

        sim_feature = self.component.create_feature_component(feature_id=feature_id)
        mapped_sim_feature = self.user.mapper.create_sim_component(sim_feature,
                                                                   data_model=self.user.data_model)

        FeatureCls = self.user.mapper.get_mapped_class('feature')
        if mapped_sim_feature not in FeatureCls.cls_instances:
            FeatureCls.cls_instances.append(mapped_sim_feature)

        ui.notify(f'Component {mapped_sim_feature.name} with ID {mapped_sim_feature.id} created!')
        self.user.grid_view.ui_content.refresh()
        self.user.geometry_manager.ui_content.refresh()

    async def show_feature_component_detail(self, props):
        feature_id = props.args['key']
        Feature = self.user.mapper.get_mapped_class('feature')
        feature = self.component.features[feature_id]

        if not hasattr(feature, 'feature_ids'):
            return

        components = [x for x in Feature.cls_instances if x.uuid in feature.feature_ids]

        if components:
            if components.__len__() > 1:
                result = await ChooseComponentDialog(components=components)
                show_detail(result)

            else:
                await sleep(0.1)
                show_detail(components[0])
        else:
            return


view_manager.views['free_cad_geometry'] = FCGeometryDetailView


class FeatureDetailView(ComponentDetailBaseView):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scene = None

    @ui.refreshable
    def ui_content(self, *args, **kwargs):
        super().ui_content(*args, **kwargs)

        self.three_d_view()

        with ui.row():
            ui.label('FreeCAD Geometry File:')
            ui.label(self.component.fc_obj_file.name)
            ui.button(on_click=lambda e: show_detail(self.component.fc_obj_file),
                      icon='launch')

        with ui.grid(columns=6):

            ui.label('ID:')
            ui.label('Name:')
            ui.label('Type:')
            ui.label('Label:')
            ui.label('Area:')
            ui.label('Volume:')

            ui.label(str(self.component.fc_obj_file_id))
            ui.label(self.component.name)
            ui.label(self.component.fc_obj_file.features[self.component.fc_obj_file_id].TypeId)
            ui.label(self.component.fc_obj_file.features[self.component.fc_obj_file_id].Label)

            try:
                area = self.component.fc_obj_file.features[self.component.fc_obj_file_id].Shape.Area
            except Exception as e:
                area = 'N/A'
            ui.label(f'{area:.3f}')

            try:
                volume = self.component.fc_obj_file.features[self.component.fc_obj_file_id].Shape.Volume
            except Exception as e:
                volume = 'N/A'
            ui.label(f'{volume:.3f}')

        with ui.button(icon='auto_fix_high', on_click=self.create_simgeo):
            ui.tooltip('Create SimGeo Geometry from this feature')

    @ui.refreshable
    def three_d_view(self):

        with ExtendedScene(background_color='#222').classes('w-full') as self.scene:

            scene = self.scene
            feature = self.component.fc_obj_file.features[self.component.fc_obj_file_id]
            group, (x_height_i, y_height_i, z_height_i) = display_feature(feature, scene)
            scene.move_camera(x=x_height_i, y=-y_height_i, z=z_height_i * 2, duration=2)

    @property
    def logger(self):
        return self.user.logger

    def create_simgeo(self, props):

        n = ui.notification(timeout=None)
        n.spinner = True
        n.message = f'Creating SimGeo Geometry from feature {self.component.name}...'
        logger.info(f'Creating SimGeo Geometry from feature {self.component.name}...')

        try:

            feature = self.component.fc_obj_file.features[self.component.fc_obj_file_id]

            new_geo_model = GeometryModel(name=f'Simgeo feature {feature.Name}',
                                          object_mapper=self.user.mapper,
                                          data_model=self.user.data_model)

            self.component.to_simgeo(geo_model=new_geo_model)

            self.logger.info(f'Successfully created SimGeo Geometry from feature {self.component.name}')
            n.message = 'Done!'
        except Exception as e:
            self.logger.error(f'Error creating SimGeo Geometry from feature {self.component.name}: {e}')
            n.message = f'Error creating SimGeo Geometry from feature {self.component.name}: {e}'
        finally:

            n.spinner = False
            # self.method(*args, **kwargs)
            n.dismiss()
            self.user.geometry_manager.ui_content.refresh()
            self.user.grid_view.ui_content.refresh()


view_manager.views['feature'] = FeatureDetailView


class ChooseComponentDialog(ui.dialog):

    def __init__(self,
                 components,
                 **kwargs):

        self.components = components

        super().__init__(value=True)
        self.props("persistent")
        with self, ui.card():

            with ui.row():
                ui.button('Ok', on_click=lambda e, option=self.selected_component: self.submit(option))
                ui.button('Cancel', on_click=lambda e: self.submit(None))

    @property
    def options(self):
        return [f'{comp.name} {comp.id}' for comp in self.components]

    @property
    def selected_component(self):
        return next((comp for comp in self.components if f'{comp.name} {comp.id}' == self.value), None)
