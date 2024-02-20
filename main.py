import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from config import BOT_TOCKEN
from all_text import All_Text
import keyboards


bot = Bot(token=BOT_TOCKEN)
dp = Dispatcher()


@dp.message(F.text == 'Назад')
@dp.message(Command("start"))
async def handle_start(message: types.Message):

    kb = keyboards.start_keyboard
    keyboard = types.ReplyKeyboardMarkup(
       keyboard=kb,
       resize_keyboard=True,
       input_field_placeholder=All_Text.keyboard_text_start 
    )

    await message.answer(
        text=f"Приветствую, {message.from_user.full_name}!" + All_Text.start_message,
        reply_markup=keyboard
    )
    await message.answer(text=All_Text.second_start_message)


@dp.message(F.text == All_Text.button_graph)
async def build_graph(message: types.Message):
    kb = keyboards.graph_kpv_keyboard
    keyboard = types.ReplyKeyboardMarkup(
       keyboard=kb,
       resize_keyboard=True,
       input_field_placeholder=All_Text.keyboard_text_start 
    )
    await message.answer(
        text="Построение графика КПВ",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())