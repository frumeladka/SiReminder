from aiogram import Router, types, F
from aiogram.filters import Command
from db import add_reminder
from datetime import datetime
from dialogs import START, ADD, TODAY, TOMORROW, WEEK, HELP, SCHEDULE, schedule

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(START, parse_mode="HTML")

@router.message(Command("add"))
async def add_handler(message: types.Message):
    try:
        s = message.text.strip()
        text, datetime_str = s[:-16], s[-16:]
        dt = datetime.fromisoformat(datetime_str.strip())
        add_reminder(
            user_id=message.from_user.id,
            text=text.strip(),
            datetime_str=dt
        )
        await message.answer(ADD[0])
    except Exception as e:
        await message.answer(ADD[1])
        print(e)

@router.message(Command("today"))
async def today_handler(message: types.Message):
    await message.answer(TODAY + '\n' + schedule[0], parse_mode="HTML")



@router.message(Command("tomorrow"))
async def tomorrow_handler(message: types.Message):
    await message.answer(TOMORROW + '\n' + schedule[1], parse_mode="HTML")


@router.message(Command("week"))
async def week_handler(message: types.Message):
    await message.answer(WEEK + '\n' + schedule[0] + '\n' + schedule[1] + '\n' + schedule[2] + '\n' + schedule[3] + '\n' + schedule[4] + '\n' + schedule[5] + '\n' + schedule[6], parse_mode="HTML")


@router.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(HELP, parse_mode="HTML")


@router.message(Command("schedule"))
async def schedule_handler(message: types.Message):
    await message.answer(SCHEDULE)
