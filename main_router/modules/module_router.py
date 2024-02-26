from aiogram import Router

from .indev_module import router as indev_router
from .graph_module import router as graph_router
from .filter_module import router as fiter_router
from .help_module import router as help_router
from .ep_module import router as equilibrium_router

router = Router(name=__name__)

router.include_router(indev_router)
router.include_router(fiter_router)
router.include_router(graph_router)
router.include_router(equilibrium_router)
router.include_router(help_router)