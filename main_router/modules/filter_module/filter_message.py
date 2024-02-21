from aiogram import Router, F, types
from random import randint

router = Router(name=__name__)

@router.message(F.sticker)
async def answer_incorrect_message(message: types.Message):
    stickers =[
        types.FSInputFile("photo\sitcker1.jpg"),
        types.FSInputFile("photo\sitcker2.jpg"),
        types.FSInputFile("photo\sitcker3.jpg"),
        types.FSInputFile("photo\sitcker4.jpg"),
        types.FSInputFile("photo\sitcker5.jpg"),
        types.FSInputFile("photo\sitcker6.jpg"),
        types.FSInputFile("photo\sitcker7.jpg")
    ]
    
    sticker = stickers[randint(0, 6)]

    await message.answer_sticker(sticker=sticker)