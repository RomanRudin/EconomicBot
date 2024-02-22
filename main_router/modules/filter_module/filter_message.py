from aiogram import Router, F, types
from random import randint

from all_text import All_Text
from main_router.modules.help_module import help
from main_router.modules.graph_module import graph

router = Router(name=__name__)


stickers =[
        types.FSInputFile("photo\stickers\sitcker1.jpg"),
        types.FSInputFile("photo\stickers\sitcker2.jpg"),
        types.FSInputFile("photo\stickers\sitcker3.jpg"),
        types.FSInputFile("photo\stickers\sitcker4.jpg"),
        types.FSInputFile("photo\stickers\sitcker5.jpg"),
        types.FSInputFile("photo\stickers\sitcker6.jpg"),
        types.FSInputFile("photo\stickers\sitcker7.jpg")
    ]


sticker_for_voice = types.FSInputFile("photo\stickers\sticker_for_voice.jpg")
sticker_for_voice_note = types.FSInputFile("photo\stickers\\video_mes.jpg")


@router.message(F.sticker)
async def sticker_react(message: types.Message):
    
    sticker = stickers[randint(0, 6)]

    await message.answer_sticker(sticker=sticker)


@router.message(F.video_note)
async def voice_mes_react(message: types.Message):
    await message.answer_sticker(sticker_for_voice_note)


@router.message(F.voice)
async def voice_react(message: types.Message):
    await message.answer_sticker(sticker_for_voice)


@router.message(~F.text)
async def non_text_react(message: types.Message):
    await message.answer(All_Text.incorrect_message_text)


@router.message(~F.text.endswith('.'))
async def text_react(message: types.Message):

    if help.help_flag and message.text in "1234":
        id_mes = int(message.text)
        if 1 <= id_mes <= 4:
            await help.info_message(message, id_mes)
            
    elif graph.make_graph_flag and message.text[0] == "-":
        await message.answer(All_Text.incorrect_negative_num_text)

    elif graph.make_graph_flag and message.text[0] in "0123456789":
        try:
            int(message.text)
            await graph.create_graph(message)
        except ValueError:
            await message.answer(All_Text.incorrect_num_text)
    
    elif graph.make_graph_flag or help.help_flag:
        await message.answer(All_Text.incorrect_data_text)

    else:
        await message.answer(All_Text.incorrect_command)