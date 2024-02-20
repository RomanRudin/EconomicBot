__all__ = ("router", )

from aiogram import Router

from .modules import router as module_router

router = Router(name=__name__)

router.include_router(module_router)