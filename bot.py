"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging, ephem
import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t2.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}

# global variables for cities game 
cities_game = False # game mode
cities_set  = None  # set of available cities
prev_city   = None  # the latter city of the mentioned ones


def greet_user(bot, update):
    update.message.reply_text('Привет!')


def talk_to_me(bot, update):
    user_text = update.message.text
    if cities_game:
        city = cities(user_text.lower())
        update.message.reply_text(city)
    else:
        update.message.reply_text(user_text[::-1].swapcase())


# новая функция
def pl_in_con(bot, update):
    planet = update.message.text
    today = str(datetime.date.today())        
    try:
        planet = planet.split()[1].capitalize()
        assert planet in ("Sun", "Mercury", "Venus", "Moon", "Mars", 
                          "Jupiter", "Saturn", "Uranus", "Neptune", 
                          "Pluto")
        planet = getattr(ephem, planet)(today)
    except:
        update.message.reply_text("Ошибка ввода")
    else:
        constel = ephem.constellation(planet)
        update.message.reply_text(constel[1])


def wordcount(bot, update):
    words = str(len(update.message.text.split()[1:]))
    declensions = {
        'слов':  ('0', '5', '6', '7', '8', '9', '11', '12', '13', '14'), 
        'слово': ('1', ), 
        'слова': ('2', '3', '4'),
        }
    if words.endswith(declensions['слов']):
        declension = 'слов'
    elif words.endswith(declensions['слово']):
        declension = 'слово'
    else:
        declension = 'слова'
    update.message.reply_text(f'{words} {declension}')


def moon(bot, update):
    today = str(datetime.date.today())
    full_moon = datetime.datetime.strptime(str(ephem.next_full_moon(today)), '%Y/%m/%d %H:%M:%S')
    _date = full_moon.strftime('%d.%m.%Y')
    _time = full_moon.strftime('%H:%M:%S')
    update.message.reply_text(f'Следующее полнолуние случится {_date} в {_time}')


def cities_on(bot, update):
    import json
    import os
    global cities_game
    cities_game = True  # initialize game mode
    global cities_set
    print(os.getcwd())
    try:
        with open(r"C:\projects\andy's_bot\cities01.rst", 'r', encoding='utf-8') as f:
            print('opening')
            print(f)
            cities_set = set(json.loads(f.read()))
    except Exception as e:
        print(str(e))
        raise
    #cities_set = json.loads(open(r"C:\projects\andy's_bot\cities1.txt").read())
    print(cities_set)
    #cities_set = {'Москва', 'Архангельск'}
    update.message.reply_text('*** ИГРАЕМ! ***\n\n'
                              'Вводите названия городов на русском языке.\n'
                              'Регистр букв не важен:\n'
                              '"Амстердам" = "аМСТерДам".\n'
                              'Чтобы закончить игру, введите /stopgame'
                             )


def cities_off(bot, update):
    global cities_game
    cities_game = False
    global cities_set
    cities_set  = None  # default value
    global prev_city
    prev_city   = None  # default value
    update.message.reply_text('*** ИГРА ОКОНЧЕНА ***')


def cities(user_city): # game's algorithm
    global cities_game
    global cities_set
    global prev_city
    if prev_city and user_city[0] != prev_city[-1]:
        return f'*** НЕПРАВИЛЬНО! ***\n\nПервая буква должна быть "{prev_city[-1].upper()}".'
    elif user_city not in cities_set:
        return ('*** НЕПРАВИЛЬНО! ***\n\n'
               f'Либо нет такого города: "{user_city.title()}",\n'
                'либо он уже упоминался.')
    else:
        cities_set.remove(user_city)
        for city in cities_set:
            if city[0] == user_city[-1]:
                prev_city = city
                cities_set.remove(city)
                return city.title()
    cities_game = False
    cities_set  = None
    prev_city   = None
    return 'Сдаюсь...(((((\n\n*** ИГРА ОКОНЧЕНА ***'


def calc(bot, update):
    question = update.message.text.strip()[5:]
    acceptable_opers = ('+', '-', '*', '**', '/', '//', '%', '(', ')')
    print(question)
    try:
        for character in question:
            assert character is ' ' or character.isdigit() or character in acceptable_opers
        answer = eval(question)
    except AssertionError:
        answer = (
                  'Вы ввели недопустимые операторы.\n'
                  'Допустимые операторы:\n'
                  '+ - * ** / // % ( )'
                 )
    except ZeroDivisionError:
        answer = 'На ноль делить нельзя!'
    except:
        answer = (
                  'Вы написали какой-то бред.\n'
                  'Попробуйте ещё раз.'
                 )
    update.message.reply_text(answer)


def main():
    mybot = Updater("712114941:AAHj7TiF-PbWw7pYKCRiv5nNTI0TiSAEVgQ", request_kwargs=PROXY)
    
    dp = mybot.dispatcher

    commands = {
        'start'         : greet_user,
        'planet'        : pl_in_con,    # planet in constellation
        'wordcount'     : wordcount,    # counting words
        'next_full_moon': moon,         # when the next full moon?
        'cities'        : cities_on,    # start playing cities
        'stopgame'      : cities_off,   # stop playing cities
        'calc'          : calc,         # calculator
        }

    for command, function in commands.items():
        dp.add_handler(CommandHandler(command, function))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) 
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
