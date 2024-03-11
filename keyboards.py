""" 
Здесь находятся все шаблоны клавиатур,

функции для генерации клавиатур и для обновления клавиатуры в меню настроек
"""

from aiogram import types

import all_text
import config


keyboards = {
    "start_keyboard" : [
        [
            types.KeyboardButton(text=all_text.button_graph),
            types.KeyboardButton(text=all_text.button_equilibrium_point),
        ],
        [
            types.KeyboardButton(text=all_text.button_deficit_and_surplus),
            types.KeyboardButton(text=all_text.button_profit),
        ]
    ],

    "back_keyboard" : [
        [types.KeyboardButton(text=all_text.button_back_to_menu)]
    ],

    "help_keyboard" : [
        [
            types.KeyboardButton(text=all_text.button_help_1),
            types.KeyboardButton(text=all_text.button_help_2)
        ],
        [
            types.KeyboardButton(text=all_text.button_help_3),
            types.KeyboardButton(text=all_text.button_help_4)
        ],
        [
            types.KeyboardButton(text=all_text.button_back_to_menu)
        ]
    ],

    "settings_keyboard" : [
        [
            types.KeyboardButton(
                text=all_text.button_switch_solution['ep'][config.solution_ep_flag]
            ),
            types.KeyboardButton(
                text=all_text.button_switch_solution['def_surp'][config.solution_def_surp_flag]
            )
        ],
        [
            types.KeyboardButton(
                text=all_text.button_switch_solution['profit'][config.solution_progit_flag]
            )
        ],
        [
            types.KeyboardButton(text=all_text.button_back_to_menu)
        ]
    ],

    "profit_keyboard" : [
        [
            types.KeyboardButton(text=all_text.button_none_costs)
        ],
        [
            types.KeyboardButton(text=all_text.button_back_to_menu)
        ]
    ]
}


def update_settings_keyboard():
    """ обновление клавиатуры в меню настроек """

    keyboards["settings_keyboard"] =[
        [
            types.KeyboardButton(
                text=all_text.button_switch_solution['ep'][config.solution_ep_flag]
            ),
            types.KeyboardButton(
                text=all_text.button_switch_solution['def_surp'][config.solution_def_surp_flag]
            )
        ],
        [
            types.KeyboardButton(
                text=all_text.button_switch_solution['profit'][config.solution_progit_flag]
            )
        ],
        [
            types.KeyboardButton(text=all_text.button_back_to_menu)
        ]
    ]


def create_keyboard(keyboard_name: str) -> types.ReplyKeyboardMarkup:
    """ генерация клавиатур по названию из списка keyboards """    

    kb = keyboards[keyboard_name]

    keyboard = types.ReplyKeyboardMarkup(
       keyboard=kb,
       resize_keyboard=True,
       input_field_placeholder=all_text.keyboard_text_start
    )
    return keyboard
