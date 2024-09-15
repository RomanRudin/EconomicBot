"""
Обработка нажатия кнопки 'Построить общую КПВ.',
вызов функции для создания графика,
вывод графика
"""

from aiogram import F, Router, types

from keyboards import create_keyboard
from main_router.modules.graph_module.create_graph import draw_graph

import all_text
import config

router = Router(name=__name__)


counter = 1
request_data = []


@router.message(F.text == all_text.button_graph)
async def change_flag(message: types.Message):
    """ обработка нажатия кнопки 'Построить общую КПВ.' """

    await message.answer(
        text="Построение графика КПВ",
        reply_markup=create_keyboard(keyboard_name="back_keyboard")
    )
    await message.answer(
        text=all_text.graph_request[0]
    )

    config.make_graph_flag = True


async def create_graph(message: types.Message):
    """ обработка введенных данных, вывод графика КПВ """

    global counter, request_data

    if counter < 4:
        await message.answer(
            text=all_text.graph_request[counter]
        )


    arg = int(message.text)
    if arg > 10000:
        arg = 9999

    request_data.append(arg)
    counter += 1

    if len(request_data) == 4:
        graph_path = draw_graph(
            request_data[0],
            request_data[1],
            request_data[2],
            request_data[3]
        )

        photo = types.FSInputFile(graph_path)
        await message.answer_photo(
            photo=photo,
            caption="Ваш график готов!"
        )


        config.make_graph_flag = False
        counter = 1
        request_data = []


        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )
