import requests
from pymessenger.bot import Bot

class Responses():
	bot=""
	def __init__(self,access_token):
		bot = Bot(access_token)
		self.bot = bot

	def saluda(self, sender_id):
		text = "HOLA :D"
		self.bot.send_text_message(sender_id,text)


