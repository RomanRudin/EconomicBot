from aiogram import F, Router, types
from aiogram.filters import Command
from os import system 

from main_router.modules.graph_module import graph
from main_router.modules.ep_module import equilibrium_point as ep
from main_router.modules.def_surp_module import deficit_and_surplus as def_surp
from main_router.modules.profit_module import profit
from keyboards import create_keyboard

import all_text
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

    profit.request_counter = 1
    profit.coefficients = []
    config.calculate_profit_flag = False
    config.profit_vc_flag = False
    config.profit_fc_flag = False

    config.calculate_profit_flag = False

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

    print(f"{'-'*10}profit{'-'*10}")
    print(f"counter: {profit.request_counter}")
    print(f"coefficients: {profit.coefficients}")

    print(f"{'-'*13}flags{'-'*13}")
    print(f"calculate_ep_flag:--------{config.calculate_ep_flag}")
    print(f"make_graph_flag:----------{config.make_graph_flag}")
    print(f"determine_def_surp_flag:--{config.determine_def_surp_flag}")
    print(f"profit_flag---------------{config.calculate_profit_flag}")
    print(f"profit_vc_flag------------{config.profit_vc_flag}")
    print(f"profit_fc_flag------------{config.profit_fc_flag}")
    print(f"help_flag:----------------{config.help_flag}")
    print(f"settings_flag:------------{config.settings_flag}")
    print(f"solution_ep_flag:---------{config.solution_ep_flag}")
    print(f"solution_def_surp_flag:---{config.solution_def_surp_flag}")



@router.message(Command("start"))
async def handle_start(message: types.Message):

    await message.answer(
        text=(f"Приветствую, {message.from_user.full_name}{all_text.emoji['e_hello']}" + all_text.start_main_text),
        reply_markup=create_keyboard(keyboard_name="start_keyboard")
    )
    await message.answer(text=all_text.second_start_main_text)

    reset_data()


@router.message(Command("help"))
async def help(message: types.Message):
    await message.answer(
        text=all_text.help_main_text,
        reply_markup=create_keyboard(keyboard_name="help_keyboard")
    )

    reset_data()
    config.help_flag = True


@router.message(Command("data"))
async def data(message: types.Message):
    await send_date()
    await message.delete()


@router.message(Command('settings'))
async def settings(message: types.Message):

    reset_data()

    config.settings_flag = True

    all_text.update_solution_text(config.solution_ep_flag, config.solution_def_surp_flag)

    await message.answer(
        text=all_text.solution_flag_text,
        reply_markup=create_keyboard("settings_keyboard")
    )
