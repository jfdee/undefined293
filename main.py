from typing import NoReturn

from telebot import (TeleBot, types)

from config import settings


bot = TeleBot(token=settings.BOT_TOKEN)


def send_message_to_chats(text) -> NoReturn:
    """ Method for notification all bank users """
    [bot.send_message(chat_id=x, text=text) for x in settings.CHAT_LIST]


def rewrite_total_data(value: int) -> int:
    """ Method for rewrite data about bank summary """
    with open('data.txt', 'r+') as f:
        old_value_str: str = f.readline()
        try:
            old_value = int(old_value_str)
        except ValueError:
            old_value = 0
        new_value: int = old_value + value
        f.seek(0)
        f.write(str(new_value))
        f.close()
        return new_value


def is_allow_chat(chat_id: int) -> bool:
    """ Method for check chat availability """
    return chat_id in settings.CHAT_LIST


@bot.message_handler(commands=['start'])
def start(message):
    """ Start handler method """
    chat_id: int = message.chat.id
    if not is_allow_chat(chat_id=chat_id):
        bot.send_message(chat_id=chat_id, text='съебись')
        return
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    markup.add(btn1, btn2)
    bot.send_message(chat_id=chat_id, text='хуярь в банку', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    """ Text message handler method """
    chat_id: int = message.chat.id
    if not is_allow_chat(chat_id=chat_id):
        bot.send_message(chat_id=chat_id, text='съебись')
        return
    try:
        value = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, text='иди нахуй со своими буквами')
        return
    total: int = rewrite_total_data(value)
    send_message_to_chats(text=f'{message.from_user.username}\nДобавлено: {value}.\nВсего: {total}.')


if __name__ == '__main__':
    bot.polling(none_stop=True)
