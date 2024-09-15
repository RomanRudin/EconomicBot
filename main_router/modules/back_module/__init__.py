"""
Подключение роутера файла back к основному файлу пакета back_module
"""

from aiogram import Router

from .back import router as help_router

router = Router(name=__name__)

router.include_router(help_router)
