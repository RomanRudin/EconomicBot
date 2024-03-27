"""
Вывод 'пояснительной записки' согласно пункту, который выбрал пользователь
"""

from aiogram import Router, types

import all_text

router = Router(name=__name__)


async def info_message(message: types.Message) -> None:
    """ вывод 'пояснительной записки' """

    await message.answer(all_text.help_point_text[message.text])
