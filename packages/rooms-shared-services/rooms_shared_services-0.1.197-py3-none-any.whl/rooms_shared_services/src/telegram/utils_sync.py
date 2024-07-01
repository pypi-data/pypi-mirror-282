from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup


def send_telegram_bot_message(bot: TeleBot, chat_id: int, text: str, reply_markup: ReplyKeyboardMarkup | None = None):
    return bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup,
    )
