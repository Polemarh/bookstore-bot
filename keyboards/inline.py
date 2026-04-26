from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_promo_keyboard(url: str):
    link_button = InlineKeyboardButton(text="Подписаться на канал", url=url)
    sub_button = InlineKeyboardButton(text="Проверить подписку", callback_data="check_subs")
    promo_keyboard = InlineKeyboardMarkup(
                inline_keyboard=[
                    [link_button],
                    [sub_button]
                ]
    )
    return promo_keyboard