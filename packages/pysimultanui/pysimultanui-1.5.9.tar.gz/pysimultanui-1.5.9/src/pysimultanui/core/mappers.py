import os
import io
import shutil
import traceback
import sys
import importlib
import logging
from nicegui import ui, events, app
from PySimultan2.object_mapper import PythonMapper
from .method_mapper import MethodMapper
from importlib.metadata import version

from typing import TYPE_CHECKING, Any, Optional
if TYPE_CHECKING:
    from .user import User
    from ..views.detail_views import DetailView

logger = logging.getLogger('PySimultanUI')
logger.info('Imported mappers')


project_dir = os.environ.get('PROJECT_DIR', '/simultan_projects')
if not os.path.exists(project_dir):
    os.makedirs(project_dir)

app.add_static_files('/project', project_dir)


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ViewManager:

    def __init__(self, *args, **kwargs):
        self.views: dict[str, 'DetailView'] = {}

    def add_view(self,
                 taxonomy_entry_key: str,
                 view: 'DetailView'):
        self.views[taxonomy_entry_key] = view


class Mapping:

    def __init__(self,
                 user: 'User',
                 mapper: 'PythonMapper',
                 method_mapper: 'MethodMapper',
                 view_manager: 'ViewManager' = None,
                 name: str = 'Mapping'):

        self._method_mapper = None
        self._mapper = None

        self.name: str = name
        self.mapper: 'PythonMapper' = mapper
        self.method_mapper: 'MethodMapper' = method_mapper
        if self.method_mapper.mapper is None:
            self.method_mapper.mapper = self.mapper

        self.view_manager: ViewManager = view_manager if view_manager is not None else ViewManager()
        self.user: 'User' = user

    @property
    def method_mapper(self) -> 'MethodMapper':
        return self._method_mapper

    @method_mapper.setter
    def method_mapper(self, value: 'MethodMapper') -> None:
        self._method_mapper = value
        if self._method_mapper is not None:
            if self._method_mapper.mapper is None:
                self._method_mapper.mapper = self.mapper

    @property
    def mapper(self) -> 'PythonMapper':
        return self._mapper

    @mapper.setter
    def mapper(self, value: 'PythonMapper') -> None:
        self._mapper = value
        if self._method_mapper is not None:
            if self._method_mapper.mapper is None:
                self._method_mapper.mapper = self.mapper

    def create_mapped_classes(self, *args, **kwargs):
        _ = [self.mapper.get_mapped_class(x) for x in self.mapper.registered_classes.keys()]

    def copy(self, user: 'User'):

        new_method_mapper = self.method_mapper.copy() if self.method_mapper is not None else None
        new_mapper = new_method_mapper.mapper.copy() if new_method_mapper.mapper is not None else None
        new_mapper.method_mapper = new_method_mapper
        new_mapper.clear()

        _ = [new_mapper.get_mapped_class(x) for x in new_mapper.registered_classes.keys()]

        return Mapping(mapper=new_mapper,
                       user=user,
                       method_mapper=new_method_mapper,
                       view_manager=self.view_manager,
                       name=self.name)


class MapperManager(metaclass=Singleton):

    def __init__(self,
                 available_mappings: dict[str: Mapping] = None,
                 mappings: dict['User': list[Mapping]] = None) -> None:

        self.available_mappings: dict[str: Mapping] = available_mappings if available_mappings is not None else {}
        self.mappings: dict['User':
                            list[Mapping]] = mappings if mappings is not None else {}

        self.create_mapping(name='Default')
        logger.info(f'MapperManager initialized {id(self)}')

    def create_mapping(self,
                       name: str = 'Mapping',
                       user: 'User' = None,
                       mapper: 'PythonMapper' = None,
                       method_mapper: 'MethodMapper' = None,
                       view_manager: ViewManager = None) -> Mapping:

        # if name in self.available_mappings:
        #     ui.notify(f'Mapping with name {name} already exists')
        #     raise ValueError(f'Mapping with name {name} already exists')

        if mapper is None:
            mapper = PythonMapper()
            _ = [mapper.get_mapped_class(x) for x in mapper.registered_classes.keys()]

        if method_mapper is None:
            method_mapper = MethodMapper(mapper=mapper)

        if view_manager is None:
            view_manager = ViewManager()

        mapping = Mapping(mapper=mapper,
                          user=user,
                          name=name,
                          method_mapper=method_mapper,
                          view_manager=view_manager
                          )

        self.available_mappings[name] = mapping
        return mapping

    def get_mapping(self,
                    user: 'User',
                    name: str,
                    load_undefined: bool = True
                    ) -> Mapping:

        """
        Get a mapping for a user by name. If the mapping does not exist, create it.
        :param user:
        :param name:
        :param load_undefined: load undefined components
        :return:
        """

        if name is None:
            return None

        if self.mappings.get(user, None) is None:
            self.mappings[user] = {}

        if self.mappings[user].get(name) is None:
            self.mappings[user][name] = self.available_mappings[name].copy(user=user)

        mapping = self.mappings[user][name]
        mapping.mapper.load_undefined = load_undefined

        _ = [mapping.mapper.get_mapped_class(x) for x in mapping.mapper.registered_classes.keys()]

        return mapping

    def get_mapper(self,
                   user: 'User',
                   name: str) -> 'PythonMapper':

        if self.mappings.get(user, None) is None:
            self.mappings[user] = {}

        if self.mappings[user].get(name) is None:
            self.mappings[user][name] = self.available_mappings[name].copy(user=user)

        return self.mappings[user][name].mapper

    def get_method_mapper(self,
                          user: 'User',
                          name: str) -> 'MethodMapper':

            if self.mappings.get(user, None) is None:
                self.mappings[user] = {}

            if self.mappings[user].get(name) is None:
                self.mappings[user][name] = self.available_mappings[name].copy(user=user)

            return self.mappings[user][name].method_mapper

    def get_view_manager(self, name: str) -> ViewManager:
        return self.available_mappings[name].view_manager

    def set_mapper(self,
                   user: 'User',
                   name: str,
                   mapper: 'PythonMapper') -> None:
        self.mappings[user][name].mapper = mapper
        mapper.method_mapper = self.mappings[user][name].method_mapper

    def add_package(self,
                    package: str,
                    user: 'User',
                    install: bool = True) -> None:
        try:
            new_package = importlib.import_module(package)
        except ImportError as e:
            ui.notify(f'Could not import package {package}')
            try:
                if install:
                    ui.notify(f'Installing package {package}')
                    user.logger.info(f'Installing package {package}')
                    import pip
                    pip.main(['install', package])
                    new_package = importlib.import_module(package)
            except Exception as e:
                user.logger.info(f'could not install package {package}: {e}')
                ui.notify(f'Could not install package {package}: {e}')
                return

        mapper = getattr(new_package, 'mapper', None)
        if mapper is None:
            ui.notify(f'Package {package} does not contain a mapper')
            user.logger.info(f'Package {package} does not contain a mapper')
            return

        method_mapper = getattr(new_package, 'method_mapper', None)
        if method_mapper is None:
            ui.notify(f'Package {package} does not contain a method_mapper')
            user.logger.info(f'Package {package} does not contain a method_mapper')
            return

        view_manager = getattr(new_package, 'view_manager', None)
        if view_manager is None:
            ui.notify(f'Package {package} does not contain a view_manager')
            user.logger.info(f'Package {package} does not contain a view_manager')
            return

        self.create_mapping(name=package,
                            mapper=getattr(new_package, 'mapper', None),
                            method_mapper=getattr(new_package, 'method_mapper', None),
                            view_manager=getattr(new_package, 'view_manager', None)
                            )

        if user.tool_select is not None:
            options = list(user.available_mappings.keys()) if user is not None else []
            options.sort()
            user.tool_select.set_options(options)

        user.logger.info(f'Added package {package}')
        ui.notify(f'Added ToolBox {package}')


# class MapperSelectDialog(ui.dialog):
#
#     def __init__(self, user=None) -> None:
#         super().__init__()
#         self._user = None
#
#         with self, ui.card():
#             ui.label('Select Toolbox:')
#             self.select = ui.select(options=list(self.user.available_mappings.keys()) if self.user is not None else [],
#                                     value=self.user.selected_mapper if self.user is not None else None,).classes('w-full')
#
#             with ui.checkbox('Load undefined components',
#                              value=True) as self.load_undefined:
#                 ui.tooltip('Load components that are not defined in the mapping')
#
#             with ui.row():
#                 ui.button('OK', on_click=self.select_mapper)
#                 ui.button('Cancel', on_click=self.cancel)
#
#         self.user = user
#
#     @property
#     def user(self) -> 'User':
#         return self._user
#
#     @user.setter
#     def user(self, value: 'User') -> None:
#         self._user = value
#         if self.user is not None:
#             self.select.options = list(self.user.available_mappings.keys())
#             self.select.value = self.user.selected_mapper
#         else:
#             self.select.options = []
#             self.select.value = None
#
#     def select_mapper(self, *args, **kwargs):
#
#         mapper = self.user.mapper_manager.get_mapping(self.user, self.select.value)
#         mapper.load_undefined = self.load_undefined.value
#         self.user.selected_mapper = self.select.value
#         self.user.project_manager.refresh_all_items()
#         ui.notify(f'Selected mapper: {self.user.selected_mapper}')
#         self.close()
#
#     def cancel(self, *args, **kwargs):
#         self.close()
#
#     def open(self, *args, **kwargs):
#         super().open(*args, **kwargs)


class MapperExpansion(object):

    def __init__(self, user, expansion_object) -> None:
        self._user = None
        self._expansion_object = expansion_object
        self.select = None
        self.version_label = None
        self.ui_content()
        self.user = user

    @ui.refreshable
    def ui_content(self, *args, **kwargs):
        with self._expansion_object:
            with ui.card().classes('w-full border-2 border-black-500 bg-primary'):

                ui.label('Current Toolbox:')

                self.select = ui.select(options=list(self.user.available_mappings.keys()) if self.user is not None else [],
                                        value=self.user.selected_mapper if self.user is not None else None,
                                        on_change=self.mapper_changed).classes('w-full')
                self._expansion_object.text = f'Toolbox: {self.select.value}'

                try:
                    pkg_version = version(self.select.value)
                except Exception as e:
                    pkg_version = 'Unknown'

                self.version_label = ui.label(f'Version {pkg_version}').classes('text-sm')

    @property
    def user(self) -> 'User':
        return self._user

    @user.setter
    def user(self, value: 'User') -> None:
        self._user = value
        options = list(self.user.available_mappings.keys()) if self.user is not None else []
        options.sort()
        self.select.set_options(options)
        self.select.value = self.user.selected_mapper if self.user is not None else None
        self._expansion_object.text = f'Toolbox: {self.select.value}'

    def mapper_changed(self, *args, **kwargs):
        try:
            self.user.selected_mapper = self.select.value
            self.user.project_manager.refresh_all_items()
            ui.notify(f'Selected Toolbox: {self.user.selected_mapper}')
        except Exception as e:
            error = '\n'.join(traceback.format_exception(*sys.exc_info()))
            logger.error(f'Error: {e}:\n'
                         f'{error}')
            ui.notify(f'Error: {e}:\n'
                      f'{error}')
        self._expansion_object.text = f'Toolbox: {self.select.value}'

        try:
            pkg_version = version(self.select.value)
        except Exception as e:
            pkg_version = 'Unknown'

        self.version_label.text = f'Version {pkg_version}'

    def set_options(self, options):
        self.select.set_options(options)


class AddPackageDialog(ui.dialog):

    def __init__(self, user=None) -> None:
        super().__init__()
        self._user = None
        self.package_input = None
        self.upload_card = None

        with self, ui.card():
            ui.label('Add Toolbox')
            self.package_input = ui.input(placeholder='Package name').classes('w-full')
            self.install_cb = ui.checkbox('Install package', value=True)

            ui.separator()

            self.upload_card = ui.upload(label='Upload and install package',
                                         on_upload=self.upload_package,
                                         auto_upload=True).on(
                'finish', lambda: ui.notify('Finish!')
            ).classes('max-w-full')

            with ui.row():
                ui.button('OK', on_click=self.ok)
                ui.button('Cancel', on_click=self.cancel)

        self.user = user

    @property
    def user(self) -> 'User':
        return self._user

    @user.setter
    def user(self, value: 'User') -> None:
        self._user = value

    def ok(self, *args, **kwargs):
        package_name = self.package_input.value
        self.user.mapper_manager.add_package(package_name,
                                             self.user,
                                             install=self.install_cb.value)
        self.close()

    def cancel(self, *args, **kwargs):
        self.close()

    def open(self, *args, **kwargs):
        super().open(*args, **kwargs)

    def upload_package(self,
                       e: events.UploadEventArguments,
                       *args,
                       **kwargs):

        try:
            import zipfile
            def get_package_name_from_wheel(wheel_path):
                with zipfile.ZipFile(wheel_path, 'r') as zip_ref:
                    # Extract the METADATA file; it's typically located in the *.dist-info directory
                    dist_info = [f for f in zip_ref.namelist() if f.endswith('METADATA')]
                    if not dist_info:
                        return "No METADATA file found in the wheel"

                    # Read the METADATA file to extract the package name
                    metadata_file = dist_info[0]
                    with zip_ref.open(metadata_file) as metadata:
                        for line in io.TextIOWrapper(metadata):
                            if line.startswith('Name:'):
                                return line.split(':', 1)[1].strip()
                return "Package name not found in METADATA"

            shutil.copyfileobj(e.content, open(f'{project_dir}/{e.name}', 'wb'))
            ui.notify(f'Package {e.name} uploaded!')
            import pip
            try:
                pip.main(['install', f'{project_dir}/{e.name}'])
            except Exception as e:
                ui.notify(f'Could not install package {e.name}: {e}')
                return

            ui.notify(f'Package {e.name} installed!')

            self.upload_card.delete()
            ui.label(f'Package {e.name} installed!').classes('text-green-500')

            self.package_input.value = get_package_name_from_wheel(f'{project_dir}/{e.name}')
            self.package_input.update()
        except Exception as e:
            self.user.logger.error(f'Error uploading and installing package: {e}')
            ui.notify(f'Error uploading and installing package: {e}')

        # self.ok()
