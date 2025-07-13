import json
from config import DATABASE
from datetime import datetime

def load_reminders():
    with open(DATABASE, "r") as f:
        return json.load(f)


def save_reminders(reminders):
    with open(DATABASE, "w") as f:
        json.dump(reminders, f, indent=4, ensure_ascii=False)


def add_reminder(user_id, text, datetime_str):
    reminders = load_reminders()
    reminders.append({
        "user_id": user_id,
        "text": text[5:],
        "datetime": str(datetime_str)
    })
    save_reminders(reminders)

def get_due_reminders(current_datetime):
    reminders = load_reminders()
    due = []
    remaining = []
    for r in reminders:

        #if int(datetime.timestamp(datetime.fromisoformat(r["datetime"]))) <= int(datetime.timestamp(current_datetime)):
        if datetime.fromisoformat(r["datetime"]) <= current_datetime:
            due.append(r)
        else:
            remaining.append(r)
    save_reminders(remaining)
    return due
