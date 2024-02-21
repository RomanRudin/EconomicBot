from aiogram import F, Router, types

from all_text import All_Text
from keyboards import create_keyboard
from main_router.modules.graph_module.create_graph import draw_graph


router = Router(name=__name__)


make_graph_flag = False
counter = 0
request_data = []


@router.message(F.text == All_Text.button_graph)
async def change_flag(message: types.Message):
    global make_graph_flag, counter


    await message.answer(
        text="Построение графика КПВ",
        reply_markup=create_keyboard(keyboard_name="graph_kpv_keyboard")
    )
    await message.answer(
        text=All_Text.graph_request[counter]
    )

    counter += 1
    make_graph_flag = True


@router.message(F.text == All_Text.button_back_to_menu)
async def back_to_menu(message: types.Message):
    global make_graph_flag, counter, request_data


    await message.answer(
        text="Как пожелаете",
        reply_markup=create_keyboard("start_keyboard")
    )

    make_graph_flag = False
    counter = 0
    request_data = []


@router.message(F.text)
async def get_request(message: types.Message):
    global make_graph_flag, counter, request_data


    if make_graph_flag:
        if counter < 4:
            await message.answer(
                text=All_Text.graph_request[counter]
            )

        request_data.append(int(message.text))
        counter += 1

    if len(request_data) == 4:
        graph_path = draw_graph(
            request_data[0],
            request_data[1],
            request_data[2],
            request_data[3]
        )

        photo = types.FSInputFile(graph_path)
        await message.answer_photo(
            photo=photo,
            caption="Ваш график готов!"
        )


        make_graph_flag = False
        counter = 0
        request_data = []


        await message.answer(
            text="Что-нибудь еще?",
            reply_markup=create_keyboard("start_keyboard")
        )
