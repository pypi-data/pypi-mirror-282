import os
import logging
from nicegui import app as ng_app, ui, Client
from . import user_manager


from .app.theme import frame

from .app.auth import AuthMiddleware
from .app import login

unrestricted_page_routes = {'/login'}


# ui.add_head_html("<style>" + open(Path(__file__).parent / "static_files" / "styles.css").read() + "</style>")


@ui.page('/')
def index_page(client: Client) -> None:
    frame('Home')
    login.content()
    # with frame('Home'):
    #     home.content()


@ui.page('/login')
def index_page1() -> None:
    # frame('Home')
    # with frame('Home'):
    #     pass
    login.content()


@ui.page('/project')
def index_page2(client: Client) -> None:
    # frame('Home')
    # with frame('Home'):
    #     pass

    user = user_manager.users[ng_app.storage.user['username']]
    log_handler = user.ui_log.handler
    logger = user.logger

    def connected():
        # Add log event handler
        pass

    def disconnected():
        # Remove log event handler
        user.logger.removeHandler(log_handler)

    def clear_log():
        logger.debug(f'Client cleared local event log with id: {client.id}')
        user.ui_log.log.clear()

    client.on_connect(connected)
    client.on_disconnect(disconnected)

    frame('Project')


# def on_startup():
#
#
#
# ng_app.on_startup(on_startup)


# app.on_shutdown(handle_shutdown)
def run_ui(*args, **kwargs):
    ng_app.add_middleware(AuthMiddleware)
    storage_secret = kwargs.get('storage_secret', os.environ.get('STORAGE_SECRET', 'my_secret6849'))

    # set_storage_secret(storage_secret)
    ui.run(storage_secret=storage_secret,
           title=kwargs.get('title', 'Py Simultan'),
           dark=kwargs.get('dark', False),
           reload=kwargs.get('reload', False),
           port=kwargs.get('port', 8080),
           uvicorn_logging_level=kwargs.get('uvicorn_logging_level', 'info'),
           )
    # set_storage_secret(storage_secret)

    from .core.patch_default_models import patch
    from . import user_manager
    patch(user_manager)


if __name__ in {"__main__", "__mp_main__"}:
    run_ui()
