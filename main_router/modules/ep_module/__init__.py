"""
Подключение роутера файла equilibrium_point 
к основному файлу пакета ep_module
"""

from aiogram import Router

from .equilibrium_point import router as ep_router

router = Router(name=__name__)

router.include_router(ep_router)
