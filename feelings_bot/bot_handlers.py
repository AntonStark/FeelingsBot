from datetime import datetime

import gspread
import pytz
import telebot
from telebot.types import Message

from feelings_bot.config import settings
from feelings_bot.utils import chats

gc = gspread.service_account('config/gspread/service_account.json')
sh = gc.open_by_key(settings.SPREADSHEET_ID)
bot = telebot.TeleBot(settings.TELEGRAM_API_KEY)


@bot.message_handler(commands=['start'])
def init(message: Message):
    chat_id = message.chat.id

    print(f'Run init on chat: {chat_id}')
    bot.send_message(chat_id, 'Привет! Я буду спрашивать тебя об эмоциях в случайное время дня🙂')
    chats.add_chat(chat_id)


@bot.message_handler(commands=['help'])
def handle_help(message):
    chat_id = message.chat.id
    print(f'Run handle_help on chat {chat_id}')
    bot.reply_to(message, 'Привет! Я буду спрашивать тебя об эмоциях в случайное время дня🙂')


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    chat_id = message.chat.id
    print(f'Run handle_text_message on chat {chat_id}')

    now = datetime.now(tz=pytz.timezone('Europe/Moscow'))
    date_ = now.strftime('%d.%m.%Y')
    time_ = now.strftime('%H:%M')
    emotion = message.text

    sh.sheet1.append_row([date_, time_, emotion])

    bot.send_message(message.chat.id, f'Записал: {emotion}')


def send_questions():
    print('Sending questions')
    for chat_id in chats.get_chats():
        bot.send_message(chat_id, 'Что ты чувствуешь?')
