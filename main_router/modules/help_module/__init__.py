__all__ = ("router", )

from aiogram import Router

from .help import router as help_router

router = Router(name=__name__)

router.include_router(help_router)