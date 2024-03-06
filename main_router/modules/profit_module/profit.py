from aiogram import Router, types, F

from all_text import All_Text
from keyboards import create_keyboard

import config

router = Router(name=__name__)


coefficients = []
request_counter = 1

@router.message(F.text == All_Text.button_profit)
async def start_profit(message: types.Message):
    
    config.calculate_profit_flag = True

    await message.answer(
        text="Расчет прибыли фирмы",
        reply_markup=create_keyboard("back_keyboard")
    )

    await message.answer(text=All_Text.profit_request[0])


async def get_request(message: types.Message):
    global request_counter, coefficients

    if config.profit_fc_flag:
        config.profit_fc_flag = False
        create_data_list(text_message=message.text)
        
    elif config.profit_vc_flag:
        config.profit_vc_flag = False
        create_data_list(text_message=message.text)


    if request_counter < 4:

        await message.answer(text=All_Text.profit_request[request_counter])

        if request_counter < 3:
            coefficients.append(int(message.text))


    match request_counter:
        case 2:
            config.profit_fc_flag = True
        case 3:
            config.profit_vc_flag = True
    
    request_counter += 1

    if request_counter == 5:
        
        await message.answer(text=calculate_profit(coefficients))


def create_data_list(text_message: str, check: bool = False) -> None | bool:
    global coefficients

    data_list = []
    data_value = ""
        
    if text_message == "0":
        coefficients.append(0)
        return

    if text_message.endswith(";"): text_message = text_message[:-1] 

    for i in range(text_message.count(";") + 1):

        separator_data_id = text_message.find(";")


        if separator_data_id == -1: data_value = text_message
        else: data_value = text_message[:separator_data_id]

        data_list.append(data_value)

        text_message = text_message[text_message.find(";")+1:]


    list_costs = []

    correct = False

    for data in data_list:

        separator_id = data.find(",")

        text_costs = data[:separator_id].replace(" ", "ъъъъ")
        if text_costs.startswith("ъъъъ"):
            text_costs = text_costs.replace("ъъъъ", "", 1)
        value_costs = data[separator_id+1:].replace(" ", "")

        correct = False
        if  (all(map(str.isalpha, text_costs)) and text_costs != "") and \
                    all(map(str.isdigit, value_costs)):
            correct = True

        list_costs.append((text_costs.replace("ъъъъ", " "), int(value_costs)))

    print(f"correct: {correct}")

    if check:
        if correct:
            return True
        else:
            return False
            
    coefficients.append(list_costs) 


def calculate_profit(coefficients: list):

    Q = coefficients[0]
    P = coefficients[1]
    FC_list = coefficients[2]
    VC_list = coefficients[3]

    FC = 0
    VC = 0

    FC_text = ""
    VC_text = ""


    for el in FC_list:
        FC += el[1]
        FC_text += f"{el[0]} ({el[1]} руб./единицу товара)"
        if el != FC_list[-1]:
            FC_text += ", \n"

    for el in VC_list:
        VC += el[1]
        VC_text += f"{el[0]} ({el[1]} руб./единицу товара)"
        if el != VC_list[-1]:
            VC_text += ", \n" 

    R = Q*P

    C = Q*VC + FC

    profit = R - C

    result_text = "прибыль" if profit > 0 else "убыток"

    return f"""
При реализации {Q} единиц продукции 
по {P} руб. за единицу товара и уровне переменных издержек в {VC} руб./единицу товара
(включая: {VC_text}) 
и постоянных издержек в {FC} руб. 
(включая: {FC_text}),
{result_text} составит: {abs(profit)} руб.
"""

