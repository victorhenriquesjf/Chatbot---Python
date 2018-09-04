#-*- coding: utf-8 -*-
#Chatbot
import os
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Robô do Vitão')

bot.set_trainer(ListTrainer)# aqui eu estou definindo o metodo de trainamento

for arq in os.listdir('arq'):
     chats = open('arq/'+arq,'r').readlines()
     bot.train(chats)

while True:
     request = input('Você: ')     
     response = bot.get_response(request)
     print('Bot: ',response)    
