import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    exit("Ошибка: BOT_TOKEN не найден в файле .env")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
if not CHANNEL_ID:
    exit("Ошибка: CHANNEL_ID не найден в файле .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.callback_query(F.data == "check_subs")
async def check_callback(callback: CallbackQuery):
    chat_member = await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = callback.from_user.id)
    if chat_member.status not in ["left", "kicked"]:
        await callback.message.answer("Твой промокод:")
    else:
        await callback.answer("Ты все еще не подписан!", show_allert=True)
    await callback.answer()

@dp.message(CommandStart())
async def hello(message: Message):
    await message.answer(f"Привет! {message.from_user.first_name}! Напиши /get_promo , чтобы получить скидку")

@dp.message(Command("get_promo"))
async def promo(message: Message):
    chat_member = await bot.get_chat_member(chat_id = CHANNEL_ID, user_id = message.from_user.id)
    if chat_member.status != "left" and chat_member.status != "kicked":
        await message.answer("Твой промокод:")
    else:
        link_button = InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/testtesttest232312")
        check_button = InlineKeyboardButton(text="Проверить подписку", callback_data="check_subs")
        promo_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [link_button],
                [check_button]
            ]
        )

        await message.answer("Чтобы получить скидку, нужно быть участником нашего канала!", reply_markup=promo_keyboard)

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass