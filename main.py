import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from main_router import router as main_router

from config import BOT_TOCKEN
from all_text import All_Text
from keyboards import create_keyboard
from main_router.modules.graph_module import graph


bot = Bot(token=BOT_TOCKEN)
dp = Dispatcher()

dp.include_router(main_router)


@dp.message(Command("start"))
async def handle_start(message: types.Message):

    await message.answer(
        text=f"Приветствую, {message.from_user.full_name}!" + All_Text.start_message,
        reply_markup=create_keyboard(keyboard_name="start_keyboard")
    )
    await message.answer(text=All_Text.second_start_message)

    graph.counter = 0
    graph.request_data = []
    graph.make_graph_flag = False


@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        text="Команда еще не готова :'("
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())