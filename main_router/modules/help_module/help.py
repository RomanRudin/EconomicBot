from aiogram import Router, types

import all_text

router = Router(name=__name__)


async def info_message(message: types.Message, id_info_mes: int) -> None:
    await message.answer(all_text.help_point_text[id_info_mes-1])