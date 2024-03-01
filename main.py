import asyncio

from aiogram import Bot, Dispatcher

from main_router import router as main_router
from config import BOT_TOCKEN


bot = Bot(token=BOT_TOCKEN)
dp = Dispatcher()

dp.include_router(main_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())