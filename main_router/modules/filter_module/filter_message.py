"""
Фильтрация всех сообщений от пользователя

В зависимости от типа сообщения и состояния флагов выводит определенную инфомацию, 
или вызывает соответствующие методы
"""

from aiogram import Router, F, types

from main_router.modules.help_module.help import info_message
from main_router.modules.graph_module.graph import create_graph
from main_router.modules.profit_module.profit import get_request
from main_router.modules.profit_module.profit_calculations import create_data_list
from main_router.modules.ep_module.equilibrium_point import calculate_ep
from main_router.modules.def_surp_module.deficit_and_surplus import determine_def_surp

import all_text
import config

router = Router(name=__name__)


@router.message(~F.text)
async def non_text_react(message: types.Message):
    """
    ответ на сообщения, которые не являются текстом или тем,    
    что было перечисленно выше
    """

    await message.answer(all_text.incorrect_message_text)


@router.message(~F.text.endswith('.'))
async def text_react(message: types.Message):
    """ обработка вводимых данных, если текстовое сообщение не является командой или кнопкой """

    if config.help_flag and message.text in "1234":
        id_mes = int(message.text)
        if 1 <= id_mes <= 4:
            await info_message(message)
        else:
            await message.answer(all_text.incorrect_num_text)


    elif config.settings_flag:
        await message.answer(text=all_text.incorrect_settings_data_text)


    elif config.make_graph_flag or config.calculate_ep_flag or \
        config.determine_def_surp_flag:

        try:
            num = float(message.text)

            if num == 0:
                await message.answer(text=all_text.incorrect_zero_message_text)
                await message.answer(all_text.correct_data_example)

            elif config.make_graph_flag:
                if num < 0:
                    await message.answer(all_text.incorrect_negative_num_text)
                    await message.answer(all_text.correct_data_example)
                else:
                    await create_graph(message)

            elif config.calculate_ep_flag:
                await calculate_ep(message)

            elif config.determine_def_surp_flag:
                await determine_def_surp(message)

        except ValueError:
            await message.answer(all_text.incorrect_num_text)
            await message.answer(all_text.correct_data_example)


    elif config.calculate_profit_flag:

        if not (config.profit_fc_flag or config.profit_vc_flag):
            try:
                int(message.text)
                if int(message.text) < 0:
                    await message.answer(all_text.incorrect_negative_num_text)
                    await message.answer(all_text.correct_data_example)
                else:
                    await get_request(message)

            except ValueError:
                await message.answer(all_text.incorrect_num_text)
                await message.answer(all_text.correct_data_example)

        else:
            check_data = create_data_list(text_message=message.text, check=True)

            if check_data[0]:
                await get_request(message)
            else:
                await message.answer(text=check_data[1])

    else:
        await message.answer(all_text.incorrect_command)
