from aiogram import Router

from .indev_module import router as indev_router
from .graph_module import router as graph_router

router = Router(name=__name__)

router.include_router(indev_router)
router.include_router(graph_router)