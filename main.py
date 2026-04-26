import asyncio
from aiogram import Bot, Dispatcher, F
from config import get_settings
from handlers.promo import router as promo_router
from handlers.start import router as start_router

config = get_settings()
bot = Bot(token=config.bot_token)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(promo_router)

async def main():
    try:
        await dp.start_polling(bot, config=config)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass