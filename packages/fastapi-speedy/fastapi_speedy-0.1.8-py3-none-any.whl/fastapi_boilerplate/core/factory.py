import logging

from fastapi.applications import FastAPI

from app import views as api_views
from settings import settings


def register_extensions(app: object):
    """Register third part extensions."""

    return None


def register_routers(app):
    """Register app routers."""
    app.include_router(api_views.router, prefix=settings.api_prefix)

    return None


def register_middleware(app):
    pass


def register_exceptions(app):
    """Register exceptions"""
    pass


def on_startup():
    """Startup events"""
    pass


def on_shutdown():
    """Shutdown events"""
    pass


def create_app() -> FastAPI:
    """App factory."""
    app = FastAPI(
        title=settings.app_title,
        description=settings.app_description,
        version=settings.api_version,
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )
    register_extensions(app)
    register_routers(app)
    register_middleware(app)
    register_exceptions(app)

    return app
