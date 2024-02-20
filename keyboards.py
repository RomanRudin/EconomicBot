from aiogram.types import KeyboardButton
from all_text import All_Text

start_keyboard = [
    [
        KeyboardButton(text=All_Text.button_graph),
        KeyboardButton(text="Найти точку рыночного равновесия"),
    ],
    [
        KeyboardButton(text="Расчитать объем дефицита/излишека"),
        KeyboardButton(text="Расчитать прибыль фирмы"),
    ]
]

graph_kpv_keyboard  = [
    [KeyboardButton(text="Назад")]
]