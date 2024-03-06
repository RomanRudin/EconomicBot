from aiogram import Router

from .indev_button import router as btn_router

router = Router(name=__name__)

router.include_router(btn_router)