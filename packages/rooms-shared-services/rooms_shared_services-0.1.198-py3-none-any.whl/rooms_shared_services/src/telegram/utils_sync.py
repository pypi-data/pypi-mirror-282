from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup
from telebot.util import quick_markup

def send_telegram_bot_message(bot: TeleBot, chat_id: int, text: str, reply_markup: InlineKeyboardMarkup | None = None):
    return bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup,
    )


def get_inline_keyboard_markup(keyboard_labels: list[str], callback_values: list[str], row_width: int = 1) -> InlineKeyboardMarkup:
    data_options = [{"callback_data": callback_value} for callback_value in callback_values]
    values = dict(zip(keyboard_labels, data_options))
    return quick_markup(values=values, row_width=row_width)
