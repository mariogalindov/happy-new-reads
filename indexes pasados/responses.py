import requests
from pymessenger.bot import Bot

class Responses():
	bot=""
	URL = ""
	def __init__(self,access_token):
		bot = Bot(access_token)
		self.bot = bot

	def greeting(self):
		JSON = {
			"greeting":[
			  {
			    "locale":"default",
			    "text":"Hello!"
			  }, {
			    "locale":"en_US",
			    "text":"Timeless apparel for the masses."
			  }
			]
		}
		URL="https://graph.facebook.com/v2.6/me/messages?access_token=EAAKHni1byYIBAEIoQtveXuu2zZCAnpSKGTYtb6OIQ3sbodJeZAfThQuMhpvkyCZBRUWBXgdG0l1EbdZBmQlr41eUDU1QWpAgZAUdrCFdwuDuf7LZCg0ZCh2Naun5YNdIbfdmWdG18ku3c5UeywnUz1iiRmEm9qIJOapAMY4b3AVcwZDZD"
		send=requests.post(URL,json = JSON)
		return True


	def saluda(self, sender_id):
		#crear usuario con el sender_id y guardarlo en el backend 
		text = "¡Hola! ¿Listo para empezar a leer?"
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
		calculo = str(35)
		text = "Muy bien! Debes leer " + calculo + " páginas diarias para cumplir tu objetivo"
		self.bot.send_text_message(sender_id,text)
		self.bot.send_text_message(sender_id,"¿A qué hora quieres que te recuerde leer?")

	def reading_time(self,sender_id):
		JSON = {
			"recipient":{
				"id":sender_id
						},
			"message":{
				"text" : "¿Cuánto tiempo planeas leer hoy?",
				"quick_replies" : [
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
		URL="https://graph.facebook.com/v2.6/me/messages?access_token=EAAKHni1byYIBAEIoQtveXuu2zZCAnpSKGTYtb6OIQ3sbodJeZAfThQuMhpvkyCZBRUWBXgdG0l1EbdZBmQlr41eUDU1QWpAgZAUdrCFdwuDuf7LZCg0ZCh2Naun5YNdIbfdmWdG18ku3c5UeywnUz1iiRmEm9qIJOapAMY4b3AVcwZDZD"
		send=requests.post(URL,json = JSON)
		return True

	def hora(self,sender_id):
		JSON = {
			"recipient":{
				"id":sender_id
						},
			"message":{
				"text" : "¿Listo para leer?",
				"quick_replies" : [
					{
						"content_type":"text",
						"title":"Sí :)",
						"payload":"Si",
					},
					{
						"content_type":"text",
						"title":"No",
						"payload":"No :(",
					},				]
						}
				}
		URL="https://graph.facebook.com/v2.6/me/messages?access_token=EAAKHni1byYIBAEIoQtveXuu2zZCAnpSKGTYtb6OIQ3sbodJeZAfThQuMhpvkyCZBRUWBXgdG0l1EbdZBmQlr41eUDU1QWpAgZAUdrCFdwuDuf7LZCg0ZCh2Naun5YNdIbfdmWdG18ku3c5UeywnUz1iiRmEm9qIJOapAMY4b3AVcwZDZD"
		send=requests.post(URL,json = JSON)
		return True




	def snooze_time(self,sender_id):
		JSON = {
			"recipient":{
				"id":sender_id
						},
			"message":{
				"text": "¿En cuánto tiempo quieres que te vuelva a preguntar?",
				"quick_replies" :[
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
		URL="https://graph.facebook.com/v2.6/me/messages?access_token=EAAKHni1byYIBAEIoQtveXuu2zZCAnpSKGTYtb6OIQ3sbodJeZAfThQuMhpvkyCZBRUWBXgdG0l1EbdZBmQlr41eUDU1QWpAgZAUdrCFdwuDuf7LZCg0ZCh2Naun5YNdIbfdmWdG18ku3c5UeywnUz1iiRmEm9qIJOapAMY4b3AVcwZDZD"
		send=requests.post(URL,json = JSON)
		return True
	def tiempo_lectura(self, sender_id):
			text = "Bien! :D ¿Cuántas páginas leíste hoy? "
			self.bot.send_text_message(sender_id,text)
	def resumen_diario(self, sender_id):
			text = "Excelente! :D Leíste 15 páginas más que tu objetivo diario"
			self.bot.send_text_message(sender_id,text)
			self.bot.send_text_message(sender_id,"Nos vemos mañana! :P")
