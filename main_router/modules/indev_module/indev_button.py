from aiogram import F, Router, types

import all_text

router = Router(name=__name__)

@router.message(F.text == all_text.button_indev)
async def indev_btn_answer(message: types.Message):
    video = types.FSInputFile("photo\Чувак , ты думал что то здесь будет .mp4")
    await message.answer_video(video=video)