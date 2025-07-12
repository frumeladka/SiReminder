from aiogram import Router, types, F
from aiogram.filters import Command
from db import add_reminder
from datetime import datetime
from dialogs import START

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(START, parse_mode="HTML")

@router.message(Command("add"))
async def add_handler(message: types.Message):
    try:
        text, datetime_str = message.text.split(";")
        dt = datetime.fromisoformat(datetime_str.strip())
        add_reminder(
            user_id=message.from_user.id,
            text=text.strip(),
            datetime_str=dt
        )
        await message.answer(f"✅ Напоминание сохранено")
    except Exception as e:
        await message.answer("❌ Неверный формат. Пример:\nПозвонить маме ; 2025-07-11 18:30")
        print(e)