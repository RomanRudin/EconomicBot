from aiogram import Router

from .indev_module    import router as indev_router
from .graph_module    import router as graph_router
from .filter_module   import router as fiter_router
from .help_module     import router as help_router
from .ep_module       import router as equilibrium_router
from .settings_module import router as settings_router
from .back_module     import router as back_router
from .commad_module   import router as command_router
from .def_surp_module import router as def_surp_router
from .profit_module   import router as profit_router

router = Router(name=__name__)

router.include_router(indev_router)
router.include_router(settings_router)
router.include_router(back_router)
router.include_router(command_router)
router.include_router(help_router)
router.include_router(graph_router)
router.include_router(equilibrium_router)
router.include_router(def_surp_router)
router.include_router(profit_router)
router.include_router(fiter_router)