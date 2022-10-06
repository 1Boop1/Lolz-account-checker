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

import asyncio

bot = Bot(token="")

ids = 'id.json'

admin_chat = 12345678

KD_SLEEP = 15

AUTH_TOKEN = 'TOKEN'

async def main_command():

    
    while True:

        with codecs.open(str(ids), 'r' ,encoding="UTF-8") as file:
            ides = file.readline()
            ides = str(ides)
            ides = eval(ides)
            file.close()

        for i in ides:
            try:
                print('Work')
                if i == 'users' or i == 'items':
                    pass
                else:

                    getting = requests.get('https://api.lolz.guru/market/user/' + str(i) + '/items?oauth_token=' + str(AUTH_TOKEN))
                    getting = getting.text
                    getting = json.loads(getting)
                    
                    if str(getting['items'][0]['item_id']) in ides['items']:
                        pass
                    else:
                        ides['items'].append(str(getting['items'][0]['item_id']))

                        with codecs.open(str(ids), 'w' ,encoding="UTF-8") as file:
                            file.write(str(ides))
                        
                        await bot.send_message(chat_id = admin_chat, text = 'Обнаружен новый товар! Ник: ' + str(getting['user']['username']))
                        print('New user!')
                        

                time.sleep(KD_SLEEP)
                
            except Exception as ex:
                print(ex)

asyncio.run(main_command())
