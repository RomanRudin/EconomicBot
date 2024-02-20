from aiogram import F, Router, types
from all_text import All_Text
from keyboards import create_keyboard

router = Router(name=__name__)

@router.message(F.text == All_Text.button_back_to_menu)
async def back_to_menu(message: types.Message):
    await message.answer(
        text="Как пожелаете",
        reply_markup=create_keyboard("start_keyboard")
    )

@router.message(F.text == All_Text.button_graph)
async def create_graph(message: types.Message):
    await message.answer(
        text="Построение графика КПВ",
        reply_markup=create_keyboard(keyboard_name="graph_kpv_keyboard")
    )