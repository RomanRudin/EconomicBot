from aiogram import F, Router, types
from all_text import All_Text


help_flag = False

router = Router(name=__name__)


async def info_message(message: types.Message, id_info_mes: int):
    await message.answer(All_Text.help_point_text[id_info_mes-1])