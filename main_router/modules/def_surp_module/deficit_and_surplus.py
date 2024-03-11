"""
Обработка нажатия на кнопку 'Определить дефицит/излишек.',
обработка введенных для определения дефицита/излишка,
расчет дефицита/излишка
"""

from aiogram import Router, types, F

from keyboards import create_keyboard

import all_text
import config


router = Router(name=__name__)


coefficients = []
request_counter = 1


@router.message(F.text == all_text.button_deficit_and_surplus)
async def def_and_surp(message: types.Message):
    """ обработка нажатия на кнопку 'Определить дефицит/излишек.' """

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
    """ обработка введенных данных, расчет дефицита/излишка """

    global coefficients, request_counter

    if request_counter < 5:
        await message.answer(text=all_text.def_surp_request[request_counter])
        request_counter += 1

    arg = int(float(message.text)) if int(float(message.text)) == float(message.text) \
                                        else float(message.text)
    coefficients.append(arg)

    if len(coefficients) == 5:

        a = coefficients[0]
        b = coefficients[1]
        c = coefficients[2]
        d = coefficients[3]
        e = coefficients[4]

        qd = a*e - b
        qs = c - d*e

        condition = ""
        if qd > qs:
            condition = "дефицита"
        elif qs > qd:
            condition = "излишка"
        else:
            condition = "равновесия"

        if qd < 0:
            qd = 0
        if qs < 0:
            qs = 0

        q = abs(qd - qs)

        if config.solution_def_surp_flag:
            await message.answer(
                text=all_text.create_solution_def_surp_text(a, b, c, d, e, qd, qs, q, condition)
            )
        text_1 = f"""{'Таким образом,' if config.solution_def_surp_flag else 'Итого:'}
при уровне цены в {e} денежных единиц на рынке будет ситуация {condition}. """
        text_2 = f"Размер {condition} составит: {q} ед. товара"  if condition != "равновесия" \
                                                                    else ''
        await message.answer(
                text=text_1 + text_2
        )
        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )

        config.determine_def_surp_flag = False
        request_counter = 1
        coefficients = []
