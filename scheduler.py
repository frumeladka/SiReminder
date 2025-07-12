from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from db import get_due_reminders
from aiogram import Bot
from config import TOKEN

bot = Bot(token=TOKEN)

async def check_reminders():
    now = datetime.now()
    due = get_due_reminders(now)
    for r in due:
        await bot.send_message(r["user_id"], f"🔔 Напоминание:\n{r['text']}")

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_reminders, "interval", seconds=30)
    scheduler.start()