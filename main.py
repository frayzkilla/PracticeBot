import random
import telebot
from telebot import types


datapro = []
with open("pm_pro.txt") as f:
    datapro = [row.strip() for row in f]
    
databeg = []
with open("pm_beg.txt") as f:
    databeg = [row.strip() for row in f]

def getProPowerCombo(msg):
    n = int(msg)

    s = 'Делай красиво 😈'
    i = 1
    temp_el = ''
    while i<=n:
        el = datapro[random.randint(0, len(datapro)-1)]
        if el !=temp_el:
            s = s + '\n ' + el
            temp_el = el
            i += 1
    return s

def getBegPowerCombo(msg):
    n = int(msg)

    s = 'Делай красиво 😈'
    i = 1
    temp_el = ''
    while i<=n:
        el = databeg[random.randint(0, len(databeg)-1)]
        if el !=temp_el:
            s = s + '\n ' + el
            temp_el = el
            i += 1
    return s
        
Bot = telebot.TeleBot('5658845641:AAGTQWFqnCXjOJMSsJMwmWQ2y3do9MXRzUY', parse_mode = None)

@Bot.message_handler(commands=["fourforbeg"])
def fourforbeg(m, res=False):
    Bot.send_message(m.chat.id, text=getBegPowerCombo(4))
    
@Bot.message_handler(commands=["fiveforbeg"])
def fiveforbeg(m, res=False):
    Bot.send_message(m.chat.id, text=getBegPowerCombo(5))

@Bot.message_handler(commands=["sixforbeg"])
def sixforbeg(m, res=False):
    Bot.send_message(m.chat.id, text=getBegPowerCombo(6))
    
@Bot.message_handler(commands=["sevenforbeg"])
def sevenforbeg(m, res=False):
    Bot.send_message(m.chat.id, text=getBegPowerCombo(7))



@Bot.message_handler(commands=["fourforpro"])
def fourforpro(m, res=False):
    Bot.send_message(m.chat.id, text=getProPowerCombo(4))
    
@Bot.message_handler(commands=["fiveforpro"])
def fiveforpro(m, res=False):
    Bot.send_message(m.chat.id, text=getProPowerCombo(5))

@Bot.message_handler(commands=["sixforpro"])
def sixforpro(m, res=False):
    Bot.send_message(m.chat.id, text=getProPowerCombo(6))
    
@Bot.message_handler(commands=["sevenforpro"])
def sevenforpro(m, res=False):
    Bot.send_message(m.chat.id, text=getProPowerCombo(7))


Bot.polling()