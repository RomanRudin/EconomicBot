from aiogram import F, Router, types

from keyboards import create_keyboard

import all_text
import config

router = Router(name=__name__)

coefficients = []
request_counter = 1


@router.message(F.text == all_text.button_equilibrium_point)
async def find_quilibrium_point(message: types.Message) -> None:

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
    global coefficients, request_counter

    if request_counter < 4:
        await message.answer(text=all_text.ep_request[request_counter])
        request_counter += 1

    arg = int(float(message.text)) if int(float(message.text)) == float(message.text) else float(message.text)
    coefficients.append(arg)

    if len(coefficients) == 4:
        
        A = coefficients[0]
        B = coefficients[1]
        C = coefficients[2]
        D = coefficients[3]

        P = round((C + B)/(A + D), 2)

        Q = round((A*P - B), 2)

        if config.solution_ep_flag:
            await message.answer(
                text=all_text.create_solution_ep_text(A, B, C, D, P, Q)
            )
        if Q < 0:
            await message.answer(
                text=f"При заданных коэффициентах равновесный объем Q меньше нуля. \nПрошу, попробуйте ввести другие коэффициенты.",
                reply_markup=create_keyboard("start_keyboard")
            )
        elif P < 0:
            await message.answer(
                text=f"При заданных коэффициентах равновесный цена P меньше нуля. \nПрошу, попробуйте ввести другие коэффициенты.",
                reply_markup=create_keyboard("start_keyboard")
            )
        else:
            await message.answer(
                text=f"Итого: равновесная цена равна {round(P, 2)} ден.ед., а равновесный объем равен {round(Q, 2)} ед."
            )
            await message.answer(
                text="Что-нибудь еще?",
                reply_markup=create_keyboard("start_keyboard")
            )

        config.calculate_ep_flag = False
        request_counter = 1
        coefficients = []


