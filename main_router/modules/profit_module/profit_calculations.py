"""
Файл содержит две функции:

1 - обработка вводимых данных о издержках, 
    и создание массивов 'издержек' для обработки

2 - подсчет прибыли фирмы, согласно введенным данным
"""

import all_text

def create_data_list(text_message: str, check: bool = False) -> list | tuple:
    """ обрабатывает введенные данные о издержках и создает массивы этих издержек """    

    data_list = []
    data_value = ""
    correct = False
    incorrect_text = ""

    if text_message == "0" or text_message == all_text.button_none_costs:
        if check:
            return True, incorrect_text
        return 0

    if text_message.endswith(";"):
        text_message = text_message[:-1]

    for i in range(text_message.count(";") + 1):

        separator_data_id = text_message.find(";")


        if separator_data_id == -1:
            data_value = text_message
        else:
            data_value = text_message[:separator_data_id]

        data_list.append(data_value)

        text_message = text_message[text_message.find(";")+1:]


    list_costs = []

    if len(data_list) < 6:
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

            try:
                list_costs.append((text_costs.replace("ъъъъ", " "), int(value_costs)))
            except ValueError:
                correct = False
                incorrect_text = all_text.incorrect_profit_data_text
    else:
        correct = False
        incorrect_text = all_text.incorrect_profit_num_data_text

    if check:
        if correct:
            return True, incorrect_text
        else:
            return False, incorrect_text

    return list_costs



def calculate_profit(coefficients: list) -> str:
    """ подсчет прибыли фирмы, генерация ответного сообщения """

    q = coefficients[0]
    p = coefficients[1]
    fc_list = coefficients[2]
    vc_list = coefficients[3]

    fc = 0
    vc = 0

    fc_text = ""
    vc_text = ""

    if fc_list:
        fc_text += "\n(включая: "
        for el in fc_list:
            fc += el[1]
            fc_text += f"{el[0]} ({el[1]} руб./единицу товара)"
            if el != fc_list[-1]:
                fc_text += ", \n"
        fc_text += ")"


    if vc_list:
        vc_text += "\n(включая: "
        for el in vc_list:
            vc += el[1]
            vc_text += f"{el[0]} ({el[1]} руб./единицу товара)"
            if el != vc_list[-1]:
                vc_text += ", \n"
        vc_text += ")"

    r = q*p

    c = q*vc + fc

    profit = r - c

    result_text = "прибыль" if profit > 0 else "убыток"

    return_data = [
        all_text.create_answer_profit_text(q, p, vc, fc, profit,vc_text, fc_text, result_text),
        all_text.create_solution_profit_text(profit, r, c, q, p, vc, fc, vc_list)
    ]

    return return_data
