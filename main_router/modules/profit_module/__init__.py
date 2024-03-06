from aiogram import Router

from .profit import router as profit_router

router = Router(name=__name__)

router.include_router(profit_router)