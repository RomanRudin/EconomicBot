import asyncio

from os import system

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from main_router import router as main_router

from config import BOT_TOCKEN
from all_text import All_Text
from keyboards import create_keyboard
from main_router.modules.graph_module import graph
from main_router.modules.help_module import help as help_module
from main_router.modules.ep_module import equilibrium_point as ep


bot = Bot(token=BOT_TOCKEN)
dp = Dispatcher()

dp.include_router(main_router)


def reset_data():
    graph.counter = 1
    graph.request_data = []
    graph.make_graph_flag = False

    help_module.help_flag = False

    ep.request_counter = 1
    ep.coefficients = []
    ep.calculate_ep_flag = False


async def send_date():

    clear = lambda: system('cls')
    clear()

    await asyncio.sleep(0.1)

    print(f"{'-'*10}graph{'-'*10}")
    print(f"counter: {graph.counter}")
    print(f"request_data: {graph.request_data}")
    print(f"make_graph_flag: {graph.make_graph_flag}")

    await asyncio.sleep(0.1)

    print(f"{'-'*10}help{'-'*10}")
    print(f"help_flag: {help_module.help_flag}")
    
    await asyncio.sleep(0.1)

    print(f"{'-'*10}equilibrium point{'-'*10}")
    print(f"counter: {ep.request_counter}")
    print(f"coefficients: {ep.coefficients}")
    print(f"ep_flag: {ep.calculate_ep_flag} \n")


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
async def help(message: types.Message):
    await send_date()
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )


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