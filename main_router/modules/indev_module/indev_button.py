from aiogram import F, Router, types
from all_text import All_Text

router = Router(name=__name__)

@router.message(F.text == All_Text.button_indev)
async def indev_btn_answer(message: types.Message):
    video = types.FSInputFile("photo\Чувак , ты думал что то здесь будет .mp4")
    await message.answer_video(video=video)