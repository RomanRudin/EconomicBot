from aiogram import Router, types, F

from keyboards import create_keyboard
from main_router.modules.profit_module.profit_calculations import create_data_list
from main_router.modules.profit_module.profit_calculations import calculate_profit

import all_text
import config

router = Router(name=__name__)


coefficients = []
request_counter = 1

@router.message(F.text == all_text.button_profit)
async def start_profit(message: types.Message):
    
    config.calculate_profit_flag = True

    await message.answer(
        text="Расчет прибыли фирмы",
        reply_markup=create_keyboard("back_keyboard")
    )

    await message.answer(text=all_text.profit_request[0])


@router.message(F.text == all_text.button_none_costs)
async def none_costs(message: types.Message):
    await get_request(message, True)


async def get_request(message: types.Message, skip: bool = False):
    global request_counter, coefficients

    if config.profit_fc_flag or config.profit_vc_flag:
        config.profit_fc_flag = False
        config.profit_vc_flag = False 
        text = message.text
        if skip: text = "0"
        coefficients.append(create_data_list(text_message=text))


    if request_counter < 4:

        if request_counter < 3:
            coefficients.append(int(message.text))
        
        if request_counter < 2:
            await message.answer(text=all_text.profit_request[request_counter])

        else:
            await message.answer(
                text=all_text.profit_request[request_counter],
                reply_markup=create_keyboard("profit_keyboard")
            )


    match request_counter:
        case 2:
            config.profit_fc_flag = True
        case 3:
            config.profit_vc_flag = True
    
    request_counter += 1

    if request_counter == 5:
        
        await message.answer(
            text=calculate_profit(coefficients)
        )

        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )
        
        request_counter = 1
        coefficients = []
        config.calculate_profit_flag = False
        config.profit_vc_flag = False
        config.profit_fc_flag = False
