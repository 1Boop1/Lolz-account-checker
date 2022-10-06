 # -*- coding: utf-8 -*-
import codecs

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle


from aiogram.utils.markdown import link

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    

from datetime import datetime, timedelta

import time

import requests

import json

bot = Bot(token="")


dp = Dispatcher(bot)

print('Subscribe Bot')

ids = 'id.json'


@dp.message_handler(commands =['start'])
async def start_func(message):
    print(message)
    await bot.send_message(chat_id = message.from_user.id, text = '*Доступные команды:\n/members - список ID для проверок\n/add [ID] - добавить участника\n/del [ID] - удалить участника.*',parse_mode = 'Markdown')

@dp.message_handler(commands =['members'])
async def members_func(message):


    g = ''
    with codecs.open(str(ids), 'r' ,encoding="UTF-8") as file:
        ides = file.readline()
        ides = str(ides)
        ides = eval(ides)
        file.close()
    
    for i in ides:
        if i == 'users' or i == 'items':
            pass
        else:
            g = g + 'ID: ' + str(i) + '\n'
    
    await message.reply('Список пользователей:\n' + str(g))

@dp.message_handler(commands =['add'])
async def add_func(message):

    text = str(message.text)
    text = text.split()
    
    with codecs.open(str(ids), 'r' ,encoding="UTF-8") as file:
        ides = file.readline()
        ides = str(ides)
        ides = eval(ides)
        file.close()
    
    ides[str(text[1])] = 0

    with codecs.open(str(ids), 'w' ,encoding="UTF-8") as file:
        file.write(str(ides))
    
    await message.reply('Пользователь добавлен')

@dp.message_handler(commands =['del'])
async def del_func(message):

        
    text = str(message.text)
    text = text.split()
    
    with codecs.open(str(ids), 'r' ,encoding="UTF-8") as file:
        ides = file.readline()
        ides = str(ides)
        ides = eval(ides)
        file.close()
    
    del ides[str(text[1])]

    with codecs.open(str(ids), 'w' ,encoding="UTF-8") as file:
        file.write(str(ides))
    
    await message.reply('Пользователь Удалён')
    

    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)


#2 goda staja / zakazivaite skripti