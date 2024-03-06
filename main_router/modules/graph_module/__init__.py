from aiogram import Router

from .graph import router as graph_router

router = Router(name=__name__)

router.include_router(graph_router)