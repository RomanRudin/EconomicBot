from aiogram import F, Router, types
from aiogram.filters import Command
from os import system 

from all_text import All_Text
from main_router.modules.graph_module import graph
from main_router.modules.ep_module import equilibrium_point as ep
from main_router.modules.def_surp_module import deficit_and_surplus as def_surp
from keyboards import create_keyboard

import config

router = Router(name=__name__)


def reset_data():
    graph.counter = 1
    graph.request_data = []
    config.make_graph_flag = False

    config.help_flag = False

    ep.request_counter = 1
    ep.coefficients = []
    config.calculate_ep_flag = False

    config.settings_flag = False

    config.determine_def_surp_flag = False


async def send_date():

    clear = lambda: system('cls')
    clear()

    print(f"{'-'*10}graph{'-'*10}")
    print(f"counter: {graph.counter}")
    print(f"request_data: {graph.request_data}")

    print(f"{'-'*10}equilibrium point{'-'*10}")
    print(f"counter: {ep.request_counter}")
    print(f"coefficients: {ep.coefficients}")
    
    print(f"{'-'*10}deficit and surplus{'-'*10}")
    print(f"counter: {def_surp.request_counter}")
    print(f"coefficients: {def_surp.coefficients}")

    print(f"{'-'*13}flags{'-'*13}")
    print(F"calculate_ep_flag:--------{config.calculate_ep_flag}")
    print(F"make_graph_flag:----------{config.make_graph_flag}")
    print(F"determine_def_surp_flag:--{config.determine_def_surp_flag}")
    print(F"help_flag:----------------{config.help_flag}")
    print(F"settings_flag:------------{config.settings_flag}")
    print(F"solution_ep_flag:---------{config.solution_ep_flag}")
    print(F"solution_def_surp_flag:---{config.solution_def_surp_flag}")



@router.message(Command("start"))
async def handle_start(message: types.Message):

    await message.answer(
        text=f"Приветствую, {message.from_user.full_name}{All_Text.emoji['e_hello']}" + All_Text.start_main_text,
        reply_markup=create_keyboard(keyboard_name="start_keyboard")
    )
    await message.answer(text=All_Text.second_start_main_text)

    reset_data()


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        text=All_Text.help_main_text,
        reply_markup=create_keyboard(keyboard_name="help_keyboard")
    )

    reset_data()
    config.help_flag = True


@router.message(Command("data"))
async def help(message: types.Message):
    await send_date()
    await message.delete()


@router.message(Command('settings'))
async def settings(message: types.Message):

    reset_data()

    config.settings_flag = True

    text = All_Text()
    text.update_solution_text(config.solution_ep_flag, config.solution_def_surp_flag)

    await message.answer(
        text=text.solution_flag_text,
        reply_markup=create_keyboard("settings_keyboard")
    )
