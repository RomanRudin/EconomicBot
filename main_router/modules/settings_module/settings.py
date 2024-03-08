from aiogram import Router, types, F

from keyboards import create_keyboard, update_settings_keyboard

import all_text
import config


router = Router(name=__name__)


@router.message((F.text == all_text.button_switch_solution["ep"][0]) | \
                (F.text == all_text.button_switch_solution["ep"][1]))
async def change_settings(message: types.Message) -> None:

    config.solution_ep_flag = 0 if config.solution_ep_flag else 1

    update_settings_keyboard()
    all_text.update_solution_text(config.solution_ep_flag, config.solution_def_surp_flag)

    await message.answer(
        text=all_text.solution_flag_text,
        reply_markup=create_keyboard("settings_keyboard")
    )


@router.message((F.text == all_text.button_switch_solution["def_surp"][0]) | \
                (F.text == all_text.button_switch_solution["def_surp"][1]))
async def change_settings(message: types.Message) -> None:

    config.solution_def_surp_flag = 0 if config.solution_def_surp_flag else 1

    update_settings_keyboard()
    all_text.update_solution_text(config.solution_ep_flag, config.solution_def_surp_flag)

    await message.answer(
        text=all_text.solution_flag_text,
        reply_markup=create_keyboard("settings_keyboard")
    )
