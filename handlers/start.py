from aiogram import Router
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Привет! {message.from_user.first_name}! Напиши /get_promo , чтобы получить скидку")

