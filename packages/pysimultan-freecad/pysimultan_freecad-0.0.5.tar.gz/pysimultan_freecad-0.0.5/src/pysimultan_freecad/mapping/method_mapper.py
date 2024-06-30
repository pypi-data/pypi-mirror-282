import os
import shutil
import tempfile
from nicegui import ui, events
from PySimultan2.files import FileInfo, create_asset_from_file
from pysimultanui import MethodMapper

method_mapper = MethodMapper()


from ..freecad.utils.im_export import import_fc_geometry


def import_project(*args, **kwargs):

    user = kwargs.get('user')
    data_model = kwargs.get('data_model')
    mapper = user.mapper

    def upload_project(e: events.UploadEventArguments,
                       *args,
                       **kwargs):

        with tempfile.TemporaryDirectory() as tmpdirname:
            temp_file_path = os.path.join(tmpdirname, e.name)
            with open(temp_file_path, 'wb') as f:
                shutil.copyfileobj(e.content, f)
        # local_path = f'/tmp/{e.name}'
        # shutil.copyfileobj(e.content, open(local_path, 'wb'))
            ui.notify(f'Project {e.name} uploaded!')
            new_fi = FileInfo(file_path=temp_file_path)

        free_cad_geometry = mapper.create_sim_component(import_fc_geometry(file_info=new_fi,
                                                                           data_model=data_model),
                                                        data_model=data_model)

        data_model.save()
        user.geometry_manager.ui_content.refresh()
        user.grid_view.ui_content.refresh()


    # choose and upload a file
    def create_new_item():
        if data_model is None:
            ui.notify('No data model selected! Please select a data model first.')
            return

        with ui.dialog() as dialog, ui.card():
            ui.upload(label='Upload asset',
                      on_upload=upload_project).on(
                'finish', lambda: ui.notify('Finish!')
            ).classes('max-w-full')
            ui.button('Cancel', on_click=lambda e: dialog.close()).classes('mt-4')

        dialog.open()

    create_new_item()


method_mapper.register_method(
    name='Import FreeCAD Project',
    method=import_project,
    add_data_model_to_kwargs=True,
    add_user_to_kwargs=True,
    kwargs={'io_bound': False}
)
