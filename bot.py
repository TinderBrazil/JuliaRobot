#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("1900667110:AAF7EFv4YotF6RygX7H3m7uKiHloXOrfU04")


@bot.message_handler(commands=["bola"])
def frase_command(m):
	if m.text == '/bola' or m.text == '/bolaGamesBrazilBot' :
		list = ["⚽️"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
@bot.message_handler(commands=["dado"])
def frase_command(m):
	if m.text == '/dado' or m.text == '/dadoGamesBrazilBot' :
		list = [""🎲"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
@bot.message_handler(commands=["boliche"])
def frase_command(m):
	if m.text == '/boliche' or m.text == '/bolicheGamesBrazilBot' :
		list = [""🎳"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
@bot.message_handler(commands=["roleta"])
def frase_command(m):
	if m.text == '/roleta' or m.text == '/roletaGamesBrazilBot' :
		list = ["🎰"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
@bot.message_handler(commands=["dardo"])
def frase_command(m):
	if m.text == '/dardo' or m.text == '/dardoGamesBrazilBot' :
		list = ["🎯"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
@bot.message_handler(commands=["basquete"])
def frase_command(m):
	if m.text == '/basquete' or m.text == '/basqueteGamesBrazilBot' :
		list = ["🏀"]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "{}".format(resposta), parse_mode='Markdown')
		
		#####Apaixonado#####
		
		
#########Start
		
def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🌟 | Canal Oficial',
                                          url='https://telegram.me/TiuMorty'))
    markup.add(types.InlineKeyboardButton('🥱 | Criador',
                                          url='https://telegram.me/TioMorty'))

    return markup


@bot.message_handler(commands=['start'])
def canal_command(m):
    bot.reply_to(m,
                    '🤖 | Este Bot Foi Criador Por : @TiuMorty',
                    reply_markup=gen_markup())
                    
                    
#####
  	
  
  
bot.polling( )
