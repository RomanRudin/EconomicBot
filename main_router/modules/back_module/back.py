from aiogram import Router, types, F

from all_text import All_Text
from main_router.modules.commad_module.commands import reset_data
from keyboards import create_keyboard

router = Router(name=__name__)


@router.message(F.text == All_Text.button_back_to_menu)
async def back_to_menu(message: types.Message):
    await message.answer(
        text="Как пожелаете",
        reply_markup=create_keyboard("start_keyboard")
    )

    reset_data()
