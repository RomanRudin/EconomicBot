from aiogram import Router, types, F

from keyboards import create_keyboard

import all_text
import config


router = Router(name=__name__)


coefficients = []
request_counter = 1


@router.message(F.text == all_text.button_deficit_and_surplus)
async def back_to_menu(message: types.Message):

    text = f"""
Определение дефицита/излишка товара
Показывать рещение: {all_text.emoji["e_condiction"][config.solution_def_surp_flag]}
"""

    await message.answer(
        text=text,
        reply_markup=create_keyboard("back_keyboard")
    )

    await message.answer(text=all_text.def_surp_request[0])

    config.determine_def_surp_flag = True


async def determine_def_surp(message: types.Message) -> None:
    global coefficients, request_counter

    if request_counter < 5:
        await message.answer(text=all_text.def_surp_request[request_counter])
        request_counter += 1

    arg = int(float(message.text)) if int(float(message.text)) == float(message.text) else float(message.text)
    coefficients.append(arg)

    if len(coefficients) == 5:
        
        A = coefficients[0]
        B = coefficients[1]
        C = coefficients[2]
        D = coefficients[3]
        E = coefficients[4]

        P = round((C + B)/(A + D), 2)

        condition = ""
        if P > E: condition = "дефицита"
        elif P < E: condition = "излишка"
        else: condition = "равновесия"

        Qd = A*E - B
        Qs = C - D*E

        if Qd < 0: Qd = 0
        if Qs < 0: Qs = 0

        Q = abs(Qd - Qs) 

        if config.solution_def_surp_flag:
            await message.answer(
                text=all_text.create_solution_def_surp_text(A, B, C, D, E, P, Qd, Qs, Q, condition)
            )
        text = f"Размер {condition} составит: {Q} ед. товара"  if condition != "равновесия" else ''
        await message.answer(
                text=f"{'Таким образом,' if config.solution_def_surp_flag else 'Итого:'} при уровне цены в {E} денежных единиц на рынке будет ситуация {condition}. {text}"
        )
        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )

        config.determine_def_surp_flag = False
        request_counter = 1
        coefficients = []
