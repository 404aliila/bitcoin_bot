# -*- coding: utf-8 -*-

import telepot
import requests
import time
import sqlite3
import bot_token

token = bot_token.token
site = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'

def handler(msg):
    chat_id = msg['from']['id']
    connection = sqlite3.connect('bitcoin.db')
    cursor = connection.cursor()
    cursor.execute('select * from users;')
    all_users = cursor.fetchall()

    for fetched_user in all_users:
        if chat_id == fetched_user[0]:
            connection.close()
            return

    cursor.execute('insert into users values(%d)' % chat_id)
    connection.commit()
    print('added : %d to database' % chat_id)
    connection.close()

bot = telepot.Bot(token)
bot.message_loop(handler)

while True:
    time.sleep(900)
    price = requests.get(site).json()
    #print (price[0]['price_usd'])
    connection = sqlite3.connect('bitcoin.db')
    cursor = connection.cursor()
    cursor.execute('select * from users;')
    all_users = cursor.fetchall()

    for i in all_users:
        try:
            bot.sendMessage(i[0], '%s$' % price[0]['price_usd'],
                            disable_notification=True)
        except:
            pass
