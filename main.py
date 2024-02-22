import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from main_router import router as main_router

from config import BOT_TOCKEN
from all_text import All_Text
from keyboards import create_keyboard
from main_router.modules.graph_module import graph
from main_router.modules.help_module import help as help_module



bot = Bot(token=BOT_TOCKEN)
dp = Dispatcher()

dp.include_router(main_router)


def reset_data():
    graph.counter = 0
    graph.request_data = []
    graph.make_graph_flag = False
    help_module.help_flag = False


def send_date():

    print(f"{'-'*10}graph{'-'*10}")
    print(f"counter: {graph.counter}")
    print(f"request_data: {graph.request_data}")
    print(f"make_graph_flag: {graph.make_graph_flag}")

    print(f"{'-'*10}help{'-'*10}")
    print(f"help_flag: {help_module.help_flag} \n")


@dp.message(Command("start"))
async def handle_start(message: types.Message):

    await message.answer(
        text=f"Приветствую, {message.from_user.full_name}!" + All_Text.start_main_text,
        reply_markup=create_keyboard(keyboard_name="start_keyboard")
    )
    await message.answer(text=All_Text.second_start_main_text)

    reset_data()


@dp.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        text=All_Text.help_main_text,
        reply_markup=create_keyboard(keyboard_name="help_keyboard")
    )

    reset_data()
    help_module.help_flag = True


@dp.message(Command("data"))
def help(message: types.Message):
    send_date()


@dp.message(F.text == All_Text.button_back_to_menu)
async def back_to_menu(message: types.Message):
    await message.answer(
        text="Как пожелаете",
        reply_markup=create_keyboard("start_keyboard")
    )

    reset_data()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())