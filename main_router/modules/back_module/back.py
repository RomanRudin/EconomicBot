from aiogram import Router, types, F

from main_router.modules.commad_module.commands import reset_data
from keyboards import create_keyboard

import all_text

router = Router(name=__name__)


@router.message(F.text == all_text.button_back_to_menu)
async def back_to_menu(message: types.Message):
    await message.answer(
        text="Как пожелаете",
        reply_markup=create_keyboard("start_keyboard")
    )

    reset_data()
