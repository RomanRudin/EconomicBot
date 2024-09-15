"""
Подключение роутера файла settings к основному файлу пакета settings_module
"""

from aiogram import Router

from .settings import router as set_router

router = Router(name=__name__)

router.include_router(set_router)
