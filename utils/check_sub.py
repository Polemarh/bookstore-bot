import asyncio
from aiogram import Bot

async def check_sub(bot: Bot, channel_id: int, user_id: int):
    member = await bot.get_chat_member(chat_id=channel_id, user_id = user_id)
    if member.status not in ["kicked", "left"]:
        return  True
    else:
        return False