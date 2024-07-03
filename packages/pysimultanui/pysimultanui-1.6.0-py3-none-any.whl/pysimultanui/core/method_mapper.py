import inspect
import typing
import collections
import asyncio
import traceback
import sys
from typing import Any, Optional
from ..config import logger
from nicegui import ui, run, app, events
from .tools import ConfirmationDialog

from PySimultan2.simultan_object import SimultanObject
from PySimultan2.object_mapper import PythonMapper


class UnknownClass(object):
    def __init__(self, *args, **kwargs):
        self.cls_name: type = kwargs.get('cls_name', 'Unknown class')
        self.cls: type = kwargs.get('cls', None)
        self.mapper = kwargs.get('mapper', None)


class UnmappedMethod(object):

    def __init__(self,
                 io_bound=False,
                 *args,
                 **kwargs):
        self.name: str = kwargs.get('name', 'Unnamed method')
        self.method = kwargs.get('method')
        self.args: list[Any] = kwargs.get('args', [])  # list with description of the arguments
        self.kwargs: dict[str:Any] = kwargs.get('kwargs', dict())  # dict with description of the keyword arguments

        self.add_data_model_to_kwargs = kwargs.get('add_data_model_to_kwargs', False)
        self.add_user_to_kwargs = kwargs.get('add_user_to_kwargs', False)
        self.io_bound = io_bound

    @property
    def user(self):
        from .. import user_manager
        return user_manager[app.storage.user['username']]

    @property
    def logger(self):
        return self.user.logger

    @property
    def data_model(self):
        return self.user.data_model

    def ui_content(self):
        with ui.item().classes('w-full h-full'):
            with ui.item_section():
                ui.label(self.name)
            with ui.item_section():
                ui.button(on_click=self.run, icon='play_circle').classes('q-ml-auto')

    async def run(self, *args, **kwargs):

        with ui.dialog() as dialog, ui.card():

            args = {}

            parameters = dict(inspect.signature(self.method).parameters)

            with ui.card():
                ui.label(f'Edit method arguments for {self.name}')

                for key, parameter in parameters.items():
                    args[key] = parameter.default if parameter.default != inspect._empty else None
                    if parameter.annotation in (int, float):
                        ui.input(label=key).bind_value(args,
                                                       key,
                                                       forward=lambda x: parameter.annotation(
                                                           x) if x is not None else None,
                                                       backward=lambda x: str(x) if x is not None else None
                                                       )

                    elif parameter.annotation is bool:
                        ui.checkbox(label=key).bind_value(args,
                                                          key)
                    elif parameter.annotation is str:
                        ui.input(label=key).bind_value(args, key)
                    elif SimultanObject in parameter.annotation.__bases__:
                        cls = self.user.mapper.mapped_classes.get(parameter.annotation._taxonomy, None)
                        if cls is None:
                            label = f'{key} (Unknown class)'
                        else:
                            options = [f'{instance.name}_{instance.id}' for instance in cls.cls_instances]

                            def backward_fcn(x):
                                if x is None:
                                    return None
                                return next((instance for instance in cls.cls_instances
                                             if f'{instance.name}_{instance.id}' == x),
                                            None)

                            ui.select(label=key,
                                      options=options,
                                      with_input=True).bind_value(args,
                                                                  key,
                                                                  backward=lambda
                                                                      x: f'{x.name}_{x.id}' if x is not None else None,
                                                                  forward=lambda x: backward_fcn(x)
                                                                  )
                    elif key in ('args', 'kwargs'):
                        continue
                    else:
                        options = []
                        all_instances = []

                        for cls in self.user.mapper.mapped_classes.values():
                            _ = [options.append(f'{x.name}_{x.id}') for x in cls.cls_instances]
                            all_instances.extend(cls.cls_instances)

                        backward_fcn = lambda x: next((instance for instance in all_instances
                                                       if f'{instance.name}_{instance.id}' == x),
                                                      None)
                        ui.select(label=key,
                                  value=f'{parameter.default.name}_{parameter.default.id}' if parameter.default is not None else 'None',
                                  options=options,
                                  with_input=True).bind_value(args,
                                                              key,
                                                              backward=lambda
                                                                  x: f'{x.name}_{x.id}' if x is not None else 'None',
                                                              forward=lambda x: backward_fcn(x))

                with ui.row():
                    ui.button('OK', on_click=lambda: dialog.submit({'ok': True, 'args': args}
                                                                   )
                              )
                    ui.button('Cancel', on_click=lambda: dialog.submit({'ok': False}))

        res = await dialog
        dialog.close()

        self.logger.info(f'Running global method {self.name}')

        if self.data_model is None:
            self.logger.error('No project loaded!')
            ui.notify('No project loaded!', type='negative')
            return

        n = ui.notification(timeout=None)
        n.spinner = True
        n.message = f'Running method {self.name}'

        if self.add_data_model_to_kwargs:
            kwargs['data_model'] = self.data_model
        if self.add_user_to_kwargs:
            kwargs['user'] = self.user

        try:
            if self.io_bound:
                await run.io_bound(self.method, *args, *self.args, **kwargs, **self.kwargs, **res['args'])
            else:
                self.method(*args, *self.args, **kwargs, **self.kwargs)
            n.type = 'positive'
            n.message = f'Successfully ran method {self.name}!'
            n.spinner = False
            await asyncio.sleep(1)
            n.dismiss()
            self.logger.info(f'Method {self.name} ran successfully!')
        except Exception as e:
            self.logger.error(f'Error running global method {self.name}:\n{e}'
                              f'{traceback.print_exception(*sys.exc_info())}')
            n.message = f'Error running method {self.name}: {e}'
            n.spinner = False
            await asyncio.sleep(2)
            n.dismiss()


class MappedMethod(object):

    def __init__(self,
                 method,
                 cls,
                 name=None,
                 args=None,
                 kwargs=None,
                 add_data_model_to_kwargs=False,
                 add_user_to_kwargs=False,
                 io_bound=False,
                 *s_args,
                 **s_kwargs):
        self.name: str = name if name is not None else 'Unnamed method'
        self.method = method
        self.cls: type = cls
        self.args: list[str] = args if args is not None else []  # list with description of the arguments
        self.kwargs: dict[
                     str:str] = kwargs if kwargs is not None else {}  # dict with description of the keyword arguments
        self.add_data_model_to_kwargs = add_data_model_to_kwargs
        self.add_user_to_kwargs = add_user_to_kwargs
        self.io_bound = io_bound

    @property
    def user(self):
        from .. import user_manager
        return user_manager[app.storage.user['username']]

    @property
    def data_model(self):
        return self.user.data_model

    @property
    def logger(self):
        return self.user.logger

    def ui_content(self):
        with ui.item():
            with ui.item_section():
                ui.label(self.name)
            with ui.item_section():
                ui.button(on_click=self.run, icon='play_circle').classes('q-ml-auto')

    async def run(self, *args, **kwargs):

        selected_instances: list[SimultanObject] = kwargs.get('selected_instances', None)
        kwargs.pop('selected_instances', None)

        self.logger.info(f'Running method {self.name} of {self.cls.__name__}')

        if selected_instances is None:
            self.logger.error('No instances selected!')
            ui.notify('No instances selected!')
            await asyncio.sleep(1)
            return

        if not all(instance._taxonomy == self.cls._taxonomy for instance in selected_instances):
            wrong_names = r' \n'.join([str((instance.name, str(instance.id))) for instance in selected_instances])
            self.logger.error(f'Not all selected instances are of the type {self.cls.__name__}!:'
                              f"{wrong_names}")

            ui.notify(f'Not all selected instances are of the type {self.cls.__name__}!:'
                      f"{wrong_names}",
                      type='negative',
                      close_button=True,
                      multi_line=True)
            await asyncio.sleep(1)
            return

        from .. import user_manager

        if user_manager[app.storage.user['username']].data_model is None:
            ui.notify('No project loaded!', type='negative')
            self.logger.error('No project loaded!')
            return

        if not selected_instances:
            ui.notify('No instances selected!')
            return

        def additional_content_fcn():
            ui.label('Selected instances:')
            for instance in selected_instances:
                with ui.row():
                    ui.label(f'{instance.name} ({instance.id})')

        if self.add_data_model_to_kwargs:
            kwargs['data_model'] = self.data_model
        if self.add_user_to_kwargs:
            kwargs['user'] = self.user

        result = await ConfirmationDialog(f'Are you sure you want to run {self.name}?',
                                          'Yes',
                                          'No',
                                          additional_content_fcn=additional_content_fcn)

        with ui.dialog() as dialog, ui.card():

            args = {}

            parameters = dict(inspect.signature(self.method).parameters)

            with ui.card():
                ui.label(f'Edit method arguments for {self.name}')

                for key, parameter in parameters.items():
                    args[key] = parameter.default if parameter.default != inspect._empty else None
                    if parameter.annotation in (int, float):
                        ui.input(label=key).bind_value(args,
                                                       key,
                                                       forward=lambda x: parameter.annotation(
                                                           x) if x is not None else None,
                                                       backward=lambda x: str(x) if x is not None else None
                                                       )

                    elif parameter.annotation is bool:
                        ui.checkbox(label=key).bind_value(args,
                                                          key)
                    elif parameter.annotation is str:
                        ui.input(label=key).bind_value(args, key)
                    elif SimultanObject in parameter.annotation.__bases__:
                        cls = self.user.mapper.mapped_classes.get(parameter.annotation._taxonomy, None)
                        if cls is None:
                            label = f'{key} (Unknown class)'
                        else:
                            options = [f'{instance.name}_{instance.id}' for instance in cls.cls_instances]

                            def backward_fcn(x):
                                if x is None:
                                    return None
                                return next((instance for instance in cls.cls_instances
                                             if f'{instance.name}_{instance.id}' == x),
                                            None)

                            ui.select(label=key,
                                      options=options,
                                      with_input=True).bind_value(args,
                                                                  key,
                                                                  backward=lambda
                                                                      x: f'{x.name}_{x.id}' if x is not None else None,
                                                                  forward=lambda x: backward_fcn(x)
                                                                  )
                    elif key in ('args', 'kwargs'):
                        continue
                    else:
                        options = []
                        all_instances = []

                        for cls in self.user.mapper.mapped_classes.values():
                            _ = [options.append(f'{x.name}_{x.id}') for x in cls.cls_instances]
                            all_instances.extend(cls.cls_instances)

                        backward_fcn = lambda x: next((instance for instance in all_instances
                                                       if f'{instance.name}_{instance.id}' == x),
                                                      None)
                        ui.select(label=key,
                                  value=f'{parameter.default.name}_{parameter.default.id}' if parameter.default is not None else 'None',
                                  options=options,
                                  with_input=True).bind_value(args,
                                                              key,
                                                              backward=lambda
                                                                  x: f'{x.name}_{x.id}' if x is not None else 'None',
                                                              forward=lambda x: backward_fcn(x))

                with ui.row():
                    ui.button('OK', on_click=lambda: dialog.submit({'ok': True, 'args': args}
                                                                   )
                              )
                    ui.button('Cancel', on_click=lambda: dialog.submit({'ok': False}))

        res = await dialog
        dialog.close()

        self.logger.info(f'User confirmed running method {self.name} of {self.cls.__name__}')

        if result == 'Yes':
            n = ui.notification(timeout=None)
            n.spinner = True
            n.message = f'Running method {self.name} of {self.cls.__name__}'
            logger.info(f'Running method {self.name} of {self.cls.__name__}')
            await asyncio.sleep(0.01)
            for instance in selected_instances:
                logger.info(f'Running method {self.name} on {instance.name} {instance.id}')

                try:
                    if self.io_bound:
                        await run.io_bound(self.method,
                                           instance,
                                           *args,
                                           *self.args,
                                           **kwargs,
                                           **self.kwargs,
                                           **res['args'])
                    else:
                        self.method(*args,
                                    *self.args,
                                    instance,
                                    **kwargs,
                                    **self.kwargs,
                                    **res['args'])

                # self.method(instance, *self.args, **self.kwargs)
                except Exception as e:
                    err = '\n'.join(traceback.format_exception(*sys.exc_info()))

                    self.logger.error(f'Error running method {self.name} on {instance.name}: {e}'
                                      f'{err}')
                    ui.notify(f'Error running method {self.name} on {instance.name}: {e}', type='negative')
                    continue

                # getattr(instance, self.name)(*self.args, **self.kwargs)
                # self.method(instance, *self.args, **self.kwargs)
            self.logger.info(f'Method {self.name} run on {len(selected_instances)} instances!')
            ui.notify(f'Method {self.name} run on {len(selected_instances)} instances!')
            n.message = 'Done!'
            n.spinner = False
            await asyncio.sleep(1)
            # self.method(*args, **kwargs)
            n.dismiss()


class MethodMapper(object):

    def __init__(self, *args, **kwargs):

        self.mapped_methods = {}
        self.unmapped_methods = []
        self.mapper = kwargs.get('mapper', None)
        self.card = None

        self.global_methods_table = None
        self.mapped_methods_table = None

        self.cls_select = None

    @property
    def selected_cls(self):
        return next((cls for cls in self.mapped_methods.keys()
                     if not isinstance(cls, UnknownClass)
                     and cls.__name__ == self.cls_select.value), None)

    @property
    def user(self):
        from .. import user_manager
        return user_manager[app.storage.user['username']]

    def register_method(self,
                        method: callable,
                        name='unnamed_method',
                        args=(),
                        kwargs={},
                        cls: type = None,
                        add_data_model_to_kwargs=False,
                        add_user_to_kwargs=False,
                        io_bound=False,
                        *s_args,
                        **s_kargs):
        if cls is None:
            self.unmapped_methods.append(UnmappedMethod(name=name,
                                                        method=method,
                                                        args=args,
                                                        add_data_model_to_kwargs=add_data_model_to_kwargs,
                                                        add_user_to_kwargs=add_user_to_kwargs,
                                                        io_bound=io_bound,
                                                        kwargs=kwargs,
                                                        *s_args,
                                                        **s_kargs),
                                         )
            return

        if cls not in self.mapped_methods:
            self.mapped_methods[cls] = []
        self.mapped_methods[cls].append(MappedMethod(cls=cls,
                                                     name=name,
                                                     method=method,
                                                     args=args,
                                                     kwargs=kwargs,
                                                     add_data_model_to_kwargs=add_data_model_to_kwargs,
                                                     add_user_to_kwargs=add_user_to_kwargs,
                                                     io_bound=io_bound,
                                                     *s_args,
                                                     **s_kargs),
                                        )

    @ui.refreshable
    def ui_content(self):

        with ui.expansion(icon='play_circle',
                          text='Methods').classes('w-full'):
            with ui.expansion(icon='public',
                              text='Global Methods').classes('w-full') as self.card:
                columns = [{'name': 'id', 'label': '#', 'field': 'id', 'sortable': True},
                           {'name': 'name', 'label': 'Name', 'field': 'name', 'sortable': True},
                           {'name': 'actions', 'label': 'Actions', 'field': 'actions', 'sortable': False}]

                rows = [{'id': i, 'name': method.name} for i, method in enumerate(self.unmapped_methods)]

                self.global_methods_table = ui.table(columns=columns,
                                                     rows=rows,
                                                     pagination={'rowsPerPage': 5, 'sortBy': 'id', 'page': 1},
                                                     row_key='id').classes('w-full h-full bordered')

                self.global_methods_table.add_slot('body-cell-actions', r'''
                                                        <q-td key="actions" :props="props">
                                                            <q-btn size="sm" color="blue" round dense
                                                                @click="$parent.$emit('run_global_method', props)"
                                                                icon="play_circle" />
                                                        </q-td>
                                                    ''')
                self.global_methods_table.on('run_global_method', self.run_global_method)

                self.resolve_classes()

            with ui.expansion(icon='public',
                              text='Mapped Methods').classes('w-full'):
                options = [cls.__name__ for cls in self.mapped_methods.keys()
                           if not isinstance(cls, UnknownClass)]
                self.cls_select = ui.select(label='Select class',
                                            options=options,
                                            value=options[0] if options else None,
                                            on_change=self.ui_method_select_content.refresh)
                self.cls_select.classes('w-full')
                self.ui_method_select_content()

    async def run_method(self, e: events.GenericEventArguments):
        selected_instances = await self.user.grid_view.selected_instances
        await self.mapped_methods[self.selected_cls][int(e.args['key'])].run(selected_instances=selected_instances)

    @ui.refreshable
    def ui_method_select_content(self):

        columns = [{'name': 'id', 'label': 'ID', 'field': 'id', 'sortable': True},
                   {'name': 'name', 'label': 'Name', 'field': 'name', 'sortable': True}]

        if self.selected_cls is None:
            rows = []
        else:
            rows = [{'id': i,
                     'name': method.name}
                    for i, method in enumerate(self.mapped_methods[self.selected_cls])]

        methods_table = ui.table(columns=columns,
                                 rows=rows,
                                 row_key='id').classes('w-full bordered')

        methods_table.add_slot('body', r'''
                                    <q-tr :props="props">
                                        <q-td v-for="col in props.cols" :key="col.name" :props="props">
                                            {{ col.value }}
                                        </q-td>
                                        <q-td auto-width>
                                            <q-btn size="sm" color="blue" round dense
                                                   @click="$parent.$emit('run_method', props)"
                                                   icon="play_circle" />
                                        </q-td>
                                    </q-tr>
                                ''')

        methods_table.on('run_method', self.run_method)

    async def run_global_method(self, e: events.GenericEventArguments):

        method = self.unmapped_methods[e.args['key']]
        await method.run()

    def resolve_classes(self):

        mapped_methods = self.mapped_methods.copy()

        for cls, methods in self.mapped_methods.items():
            if isinstance(cls, UnknownClass):
                for method in methods:
                    new_cls = self.mapper.mapped_classes.get(method.method.__qualname__.split('.')[-2], None)
                    if new_cls is None:
                        continue
                    method.cls = new_cls
                    if new_cls not in mapped_methods:
                        mapped_methods[new_cls] = []
                    mapped_methods[new_cls].append(method)
                    mapped_methods[cls].remove(method)

        self.mapped_methods = mapped_methods

    def copy(self):
        new_method_mapper = MethodMapper()
        new_method_mapper.mapped_methods = self.mapped_methods
        new_method_mapper.unmapped_methods = self.unmapped_methods
        new_method_mapper.mapper = self.mapper
        return new_method_mapper


method_mapper = MethodMapper()


def mapped_method(name=None, *args, **kwargs):
    dat_dict = {}
    dat_dict['name'] = name

    def wrapper(func):
        # vars(sys.modules[func.__module__])[func.__qualname__.split('.')
        method_mapper.register_method(method=func,
                                      name=dat_dict['name'],
                                      args=args,
                                      kwargs=kwargs,
                                      cls=UnknownClass(cls_name=func.__qualname__))
        return func

    return wrapper
