from aiogram import Router

from .commands import router as commands_router

router = Router(name=__name__)

router.include_router(commands_router)