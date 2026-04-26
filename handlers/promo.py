from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from config import Settings
from utils.check_sub import check_sub
from keyboards.inline import get_promo_keyboard

router = Router()

@router.callback_query(F.data == "check_subs")
async def check_callback(callback:CallbackQuery, bot:Bot, config: Settings):
    if await check_sub(bot, channel_id=config.channel_id, user_id=callback.from_user.id):
        await callback.message.edit_text("Спасибо! Твой промокод: ... ")
    else:
        await callback.answer("Ты все еще не подписан!", show_alert=True)
    await callback.answer()

@router.message(Command("get_promo"))
async def promo(message: Message, bot: Bot, config: Settings):
    if await check_sub(bot, channel_id=config.channel_id, user_id=message.from_user.id):
        await message.answer("Твой промокод:")
    else:
        await message.answer(
            "Чтобы получить скидку, нужно быть участником нашего канала!",
            reply_markup=get_promo_keyboard(config.channel_url)
        )

