import requests
from pymessenger.bot import Bot

class Responses():
	bot=""
	URL = ""
	def __init__(self,access_token):
		bot = Bot(access_token)
		self.bot = bot

	def saluda(self, sender_id):
		#crear usuario con el sender_id y guardarlo en el backend 
		text = "¡Hola! ¿Listo para empezar a leer hoy?"
		self.bot.send_text_message(sender_id,text)
	
	def book(self, sender_id):
		text = "¿Genial! :D ¿Qué libro quieres leer hoy? "
		self.bot.send_text_message(sender_id,text)

	def paginas(self, sender_id):
		#guardar el libro
		text = "¡Perfecto! :) ¿Cuántas páginas tiene tu libro?"
		self.bot.send_text_message(sender_id,text)

	def dias(self, sender_id):
		text = "Ok, ¿en cuántos días lo planeas leer?"
		self.bot.send_text_message(sender_id,text)

	def num_paginas(self, sender_id):
		#calculo = ir al backend y preguntar
		calculo = str(10)
		text = "Muy bien! Debes leer " + calculo + "páginas diarias para cumplir tu objetivo"

	def reading_time(self,sender_id):
		text = "¿Cuánto tiempo planeas leer hoy?"
		elemn = [
					{
						"content_type":"text",
						"title":"15 minutos",
						"payload":"15",
					},
					{
						"content_type":"text",
						"title":"30 minutos",
						"payload":"30",
					},
					{
						"content_type":"text",
						"title":"1 hora",
						"payload":"60",
					}
					]
		JSON = {
			"recipient":{
				"id":sender_id
				},
			"message":{
				"text": "¿Cuánto tiempo planeas leer hoy?",
				"quick_replies":[
					{
						"content_type":"text",
						"title":"15 minutos",
						"payload":"15",
					},
					{
						"content_type":"text",
						"title":"30 minutos",
						"payload":"30",
					},
					{
						"content_type":"text",
						"title":"1 hora",
						"payload":"60",
					}
				]
			}
		}

		requests.post(URL,json = JSON)

		self.bot.send_generic_message(recipient_id,text,elemn)

	def snooze_time(self,sender_id):
		JSON = {
			"recipient":{
				"id":sender_id
				},
			"message":{
				"text": "¿En cuánto tiempo quieres que te vuelva a preguntar?",
				"quick_replies":[
					{
						"content_type":"text",
						"title":"15 minutos",
						"payload":"POSTBACK_TEXT",
					},
					{
						"content_type":"text",
						"title":"30 minutos",
						"payload":"POSTBACK_TEXT",
					},
					{
						"content_type":"text",
						"title":"1 hora",
						"payload":"POSTBACK_TEXT",
					}
				]
			}
		}