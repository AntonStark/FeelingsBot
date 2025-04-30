"""
based on article
 https://muxtarovich.medium.com/делаем-бота-для-учета-личных-расходов-на-python-используя-google-spreadsheets-часть-2-ee17e859e1
"""
import http.client

import backoff
import pytz
import requests
import telebot  # noqa
import urllib3

from apscheduler.schedulers.background import BackgroundScheduler

from feelings_bot.bot_handlers import (
    bot,
    send_questions,
)
from feelings_bot.config import settings
from feelings_bot.utils.times import random_datetime_today

scheduler = BackgroundScheduler(timezone=pytz.utc)


@scheduler.scheduled_job(trigger='cron', hour=settings.PLAN_TIME.hour, minute=settings.PLAN_TIME.minute)
def plan_send_question():
    scheduler.add_job(
        send_questions,
        trigger='date',
        run_date=random_datetime_today(hour_min=15, hour_max=19),
    )


@backoff.on_exception(
    backoff.expo,
    (requests.exceptions.RequestException, http.client.RemoteDisconnected, urllib3.exceptions.ProtocolError),
    max_tries=8,
)
def run_bot():
    print('Starting...')
    bot.polling(none_stop=True)


if __name__ == '__main__':
    scheduler.start()
    run_bot()
