from aiogram import F, Router, types

from all_text import All_Text
from keyboards import create_keyboard

router = Router(name=__name__)


calculate_ep_flag = False
coefficients = []
request_counter = 1

@router.message(F.text == All_Text.button_equilibrium_point)
async def find_quilibrium_point(message: types.Message):
    global calculate_ep_flag

    await message.answer(
        text="Рассчет точки рыночного равновесия",
        reply_markup=create_keyboard("equilibrium_point_kb")        
    )

    await message.answer(text=All_Text.ep_request[0])

    calculate_ep_flag = True

async def calculate_ep(message: types.Message):
    global coefficients, request_counter, calculate_ep_flag

    if request_counter < 4:
        await message.answer(text=All_Text.ep_request[request_counter])
        request_counter += 1

    arg = float(message.text)
    coefficients.append(arg)

    if len(coefficients) == 4:
        
        A = coefficients[0]; B = coefficients[1]; C = coefficients[2]; D = coefficients[3]

        P = (C + B)/(A + D)

        Q = A*P - B

        await message.answer(text=f"Равновесная цена: {round(P, 2)}; Равновесный объем: {round(Q, 2)}")

        calculate_ep_flag = False
        request_counter = 1
        coefficients = []

        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )

