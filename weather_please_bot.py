# -*- coding: utf-8 -*-
"""Weather_please_bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3RhVC94xPOHati8eiUeNzFwIBYJpxxG
"""

from pyowm import OWM
from pyowm.utils.config import get_default_config
import telebot

weather_status = {'ясно': '\U00002600', 'облачно с прояснениями': '\U0001F325', 'небольшой дождь': '\U0001F4A7', 'переменная облачность': '\U000026C5', 'пасмурно': '\U00002601'}

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('708c7a4d5f293058b24273505d91e26a', config_dict)

bot = telebot.TeleBot("1378585680:AAGf7inMDvfjsf8DC51dczc_i8l-OHcVZWw")

@bot.message_handler(commands=['start', 'help'])
def commands(message):
  if message.text == '/start':
	  bot.send_message(message.from_user.id, """Привет! Я могу найти тебе погоду в нужном городе. Условие:
1. Никому не рассказывай о бойцовском клубе
2. Пиши в подобном формате 'Москва, РФ' или 'Москва'
3. Только на русском языке
У меня есть чувство, что мы с тобой сработаемся.
""")
  elif message.text == '/help':
    bot.send_message(message.from_user.id, """Смотри. Ты поможешь мне, я помогу тебе:
1. Я понимаю только в формате, подобном этому — 'Москва, РФ' или 'Москва'
2. Если я не отвечаю, то здесь две причины: или меня отключили, или ты вводишь город/страну не в том формате.
Но я тебе пишу, верно? Значит с меня взятки гладки.
""")

@bot.message_handler(content_types=['text'])
def handle_messages(message):
    global weather_status

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    now_temp = w.temperature('celsius')
    status = w.detailed_status
    bot.send_message(message.from_user.id, f'''Температура в {message.text} составляет в среднем {now_temp.get("temp")}С
На небе: {weather_status.get(status)}
''')

bot.polling()
