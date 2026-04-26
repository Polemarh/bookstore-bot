import os
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class Settings:
    bot_token: str
    channel_id: int
    channel_url: str

def get_settings():
    load_dotenv()

    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        exit("ОШИБКА: BOT_TOKEN не найден в .env")

    CHANNEL_ID = os.getenv("CHANNEL_ID")
    if not CHANNEL_ID:
        exit("ОШИБКА: CHANNEL_ID не найден в .env")
    else:
        CHANNEL_ID = int(CHANNEL_ID)

    CHANNEL_URL = os.getenv("CHANNEL_URL")
    if not CHANNEL_URL:
        exit("ОШИБКА: CHANNEL_URL не найден в .env")

    return Settings(bot_token=TOKEN, channel_id=CHANNEL_ID, channel_url=CHANNEL_URL)






