"""
Подключение роутера файла module_router к основному файлу пакета modules
"""

from aiogram import Router

from .module_router import router as main_module_router

router = Router(name=__name__)

router.include_router(main_module_router)
