"""
Обработка нажатия на кнопку 'Найти ТРР.',
обработка введенных для определения точки рыночного равновесия,
расчет параметров точки рыночного равновесия
"""

from aiogram import F, Router, types

from keyboards import create_keyboard

import all_text
import config

router = Router(name=__name__)

coefficients = []
request_counter = 1


@router.message(F.text == all_text.button_equilibrium_point)
async def find_quilibrium_point(message: types.Message) -> None:
    """ обработка нажатия на кнопку 'Найти ТРР.' """

    text = f"""
Рассчет точки рыночного равновесия
Показывать рещение: {all_text.emoji["e_condiction"][config.solution_ep_flag]}
"""

    await message.answer(
        text=text,
        reply_markup=create_keyboard("back_keyboard")
    )

    await message.answer(text=all_text.ep_request[0])

    config.calculate_ep_flag = True


async def calculate_ep(message: types.Message) -> None:
    """ обработка введенных данных, расчет точки рыночного равновесия """

    global coefficients, request_counter

    if request_counter < 4:
        await message.answer(text=all_text.ep_request[request_counter])
        request_counter += 1

    arg = int(float(message.text)) if int(float(message.text)) == float(message.text) \
                                    else float(message.text)
    coefficients.append(arg)

    if len(coefficients) == 4:

        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        d = coefficients[3]

        # qd = ap - b
        # qs = c + dp
        # ap - b = c + dp
        # ap - dp = c + b
        # p = (c + b)/(a - d)

        p = round((c + b)/(a - d), 2)

        q = round((a*p - b), 2)

        if config.solution_ep_flag:
            await message.answer(
                text=all_text.create_solution_ep_text(a, b, c, d, p, q)
            )
        if p < 0:
            text_1 = "При заданных коэффициентах равновесный цена P меньше нуля."
            text_2 = "\nПрошу, попробуйте ввести другие коэффициенты."
            await message.answer(
                text=text_1+text_2,
                reply_markup=create_keyboard("start_keyboard")
            )
        elif q < 0:
            text_1 = "При заданных коэффициентах равновесный объем Q меньше нуля."
            text_2 = "\nПрошу, попробуйте ввести другие коэффициенты."
            await message.answer(
                text=text_1+text_2,
                reply_markup=create_keyboard("start_keyboard")
            )
        else:
            text_1 =f"Итого: равновесная цена равна {round(p, 2)} ден.ед."
            text_2 =f", а равновесный объем равен {round(q, 2)} ед."
            await message.answer(
                text=text_1+text_2
            )
            await message.answer(
                text="Что-нибудь еще?",
                reply_markup=create_keyboard("start_keyboard")
            )

        config.calculate_ep_flag = False
        request_counter = 1
        coefficients = []
