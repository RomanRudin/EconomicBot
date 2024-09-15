"""
Подключение роутера файла deficit_and_surplus 
к основному файлу пакета def_surp_module
"""

from aiogram import Router

from .deficit_and_surplus import router as def_surp_router

router = Router(name=__name__)

router.include_router(def_surp_router)
