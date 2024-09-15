"""
Подключение роутера файла filter_message к основному файлу пакета filter_module
"""

from aiogram import Router

from .filter_message import router as filter_router

router = Router(name=__name__)

router.include_router(filter_router)
