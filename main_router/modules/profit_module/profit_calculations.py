import all_text

def create_data_list(text_message: str, check: bool = False) -> list | bool:
    
    data_list = []
    data_value = ""
        
    if text_message == "0" or text_message == all_text.button_none_costs:
        if check: return True
        return 0

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
            
    return list_costs



def calculate_profit(coefficients: list) -> str:

    Q = coefficients[0]
    P = coefficients[1]
    FC_list = coefficients[2]
    VC_list = coefficients[3]

    FC = 0
    VC = 0

    FC_text = ""
    VC_text = ""

    if FC_list:
        FC_text += "\n(включая: " 
        for el in FC_list:
            FC += el[1]
            FC_text += f"{el[0]} ({el[1]} руб./единицу товара)"
            if el != FC_list[-1]:
                FC_text += ", \n"
        FC_text += ")"


    if VC_list:
        VC_text += "\n(включая: " 
        for el in VC_list:
            VC += el[1]
            VC_text += f"{el[0]} ({el[1]} руб./единицу товара)"
            if el != VC_list[-1]:
                VC_text += ", \n" 
        VC_text += ")"

    R = Q*P

    C = Q*VC + FC

    profit = R - C

    result_text = "прибыль" if profit > 0 else "убыток"

    return f"""
При реализации {Q} единиц продукции 
по {P} руб. за единицу товара и уровне 
переменных издержек в {VC} руб./единицу товара {VC_text}
и постоянных издержек в {FC} руб. {FC_text},
{result_text} составит: {abs(profit)} руб.
"""

