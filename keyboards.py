from aiogram import types
from all_text import All_Text


keyboards = {
    "start_keyboard" : [
        [
            types.KeyboardButton(text=All_Text.button_graph),
            types.KeyboardButton(text=All_Text.button_equilibrium_point),
        ],
        [
            types.KeyboardButton(text=All_Text.button_indev),
            types.KeyboardButton(text=All_Text.button_indev),
        ]
    ],

    "graph_kpv_keyboard" : [
        [types.KeyboardButton(text=All_Text.button_back_to_menu)]
    ],

    "equilibrium_point_kb" : [
        [types.KeyboardButton(text=All_Text.button_back_to_menu)]
    ],

    "help_keyboard" : [
        [
            types.KeyboardButton(text=All_Text.button_help_1),
            types.KeyboardButton(text=All_Text.button_help_2)
        ],
        [
            types.KeyboardButton(text=All_Text.button_help_3),
            types.KeyboardButton(text=All_Text.button_help_4)
        ],
        [
            types.KeyboardButton(text=All_Text.button_back_to_menu)
        ]
    ]
}


def create_keyboard(keyboard_name: str) -> types.ReplyKeyboardMarkup:
    
    kb = keyboards[keyboard_name]

    keyboard = types.ReplyKeyboardMarkup(
       keyboard=kb,
       resize_keyboard=True,
       input_field_placeholder=All_Text.keyboard_text_start 
    )
    
    return keyboard