from aiogram import Router, types, F

from all_text import All_Text
from keyboards import create_keyboard, update_settings_keyboard

import config

router = Router(name=__name__)

txt = All_Text()

@router.message((F.text == txt.button_switch_solution["ep"][0]) | (F.text == txt.button_switch_solution["ep"][1]))
async def change_settings(message: types.Message) -> None:

    config.solution_ep_flag = 0 if config.solution_ep_flag else 1

    update_settings_keyboard()
    txt.update_solution_text(config.solution_ep_flag)

    await message.answer(
        text=txt.solution_flag_text,
        reply_markup=create_keyboard("settings_keyboard")
    )
