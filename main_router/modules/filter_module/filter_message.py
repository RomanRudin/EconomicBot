from aiogram import Router, F, types
from random import randint

from all_text import All_Text
from main_router.modules.help_module.help import info_message
from main_router.modules.graph_module.graph import create_graph
from main_router.modules.ep_module.equilibrium_point import calculate_ep
from main_router.modules.def_surp_module.deficit_and_surplus import determine_def_surp

import config

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


@router.message(~F.text.endswith('.') & ~F.text.startwith('/'))
async def text_react(message: types.Message):

    if config.help_flag and message.text in "1234":
        id_mes = int(message.text)
        if 1 <= id_mes <= 4:
            await info_message(message, id_mes)
        else:
            await message.answer(All_Text.incorrect_data_text)

    elif config.make_graph_flag or config.calculate_ep_flag or config.determine_def_surp_flag:
        
        if message.text[0] == "-" and config.make_graph_flag:
            await message.answer(All_Text.incorrect_negative_num_text)
            await message.answer(All_Text.correct_data_example)

        elif message.text[0] in "0123456789" or message.text[1] in "0123456789":
            try:
                float(message.text)
                if float(message.text) == 0:
                    await message.answer(text=All_Text.incorrect_zero_message_text)
                else:
                    if config.make_graph_flag:
                        await create_graph(message)
                    elif config.calculate_ep_flag:
                        await calculate_ep(message)
                    else:
                        await determine_def_surp(message)
            except:
                await message.answer(All_Text.incorrect_num_text)
                await message.answer(All_Text.correct_data_example)
                
        else:
            await message.answer(All_Text.incorrect_data_text)
            await message.answer(All_Text.correct_data_example)

    else:
        await message.answer(All_Text.incorrect_command)