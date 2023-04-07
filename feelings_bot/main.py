"""
based on article
 https://muxtarovich.medium.com/делаем-бота-для-учета-личных-расходов-на-python-используя-google-spreadsheets-часть-2-ee17e859e1
"""

from datetime import datetime

import telebot
import gspread

from feelings_bot.config import settings

bot = telebot.TeleBot(settings.TELEGRAM_API_KEY)
gc = gspread.service_account(
    filename='config/gspread/service_account.json',
)
sh = gc.open_by_key(settings.SPREADSHEET_ID)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я буду спрашивать тебя об эмоциях в случайное время дня🙂")


@bot.message_handler(content_types=['text'])
def handle_text_message(message):
    date_ = datetime.now().strftime("%d.%m.%Y")
    time_ = datetime.now().strftime("%H:%M")

    emotion = message.text

    sh.sheet1.append_row([date_, time_, emotion])

    bot.send_message(message.chat.id, f'Записал: {emotion}')


if __name__ == '__main__':
    bot.polling(none_stop=True)
