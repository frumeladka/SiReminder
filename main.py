import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import router
from scheduler import start_scheduler

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    start_scheduler()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())