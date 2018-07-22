#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
import json
from responses import Responses

app = Flask(__name__)

ACCESS_TOKEN = 'EAAKHni1byYIBAIailUcuuVrwNLqmsG7VGEK29I5erzE3gC4ZCaITZCwxZAHTqMcePZCg3Y0K8yJe2VXC80ZBNXVZBZASpZCpJrTS3dX78hbWxCbcpwAv3KxBgayN2o0fVmvCfdY6G9g4yiRh4f1jLbSJNbD7EVupxjsllHyh77wit0nQwYLgKiha'
VERIFY_TOKEN = 'one5udx4'

bot = Responses(ACCESS_TOKEN)


@app.route("/")
def index():
	return "Bot iniciado"

@app.route('/webhook', methods = ['GET', 'POST'])

def greeting():
	JSON = {
		"get_started":{
   			"payload":"<Holaa>"
  			},				
		"greeting":[
  				{
			    "locale":"es_LA",
			    "text":"Hola!"
				  }, {
				    "locale":"es_LA",
				    "text":"El chatbot que te ayudará en tu camino a la lectura."
				  }
					]
				}
			URL="https://graph.facebook.com/v2.6/me/messenger_profile?access_token=EAAKHni1byYIBAIailUcuuVrwNLqmsG7VGEK29I5erzE3gC4ZCaITZCwxZAHTqMcePZCg3Y0K8yJe2VXC80ZBNXVZBZASpZCpJrTS3dX78hbWxCbcpwAv3KxBgayN2o0fVmvCfdY6G9g4yiRh4f1jLbSJNbD7EVupxjsllHyh77wit0nQwYLgKiha"
			send=requests.post(URL,json = JSON)


def webhook():
	if request.method == 'POST':
		print("LLEGO PETICION")
		message = request.json
		print(message)
		for event in message["entry"]: #Empieza el parseo
			messaging = event["messaging"]
			for event_message in messaging:
				sender_id = event_message["sender"]["id"]
				texto = event_message["message"]["text"]
				#payload  = event_message["message"]["quick_reply"]["payload"]
				print(texto)
				if texto ==  "Hola":
					bot.saluda(sender_id)
				elif texto == "Si":
					bot.book(sender_id)
				elif texto == "El principito":
					bot.paginas(sender_id)
				elif texto == "70 páginas":
					'''
				elif "páginas" in texto:
					num_paginas = texto.split()[0]
					num_paginas = int(num_paginas)
					'''
					bot.dias(sender_id)
				elif "días" in texto:
					num_dias = texto.split()[0]
					num_dias = int(num_dias)
					bot.num_paginas(sender_id)
				elif texto == "5:44pm":
					bot.hora(sender_id)
				elif texto == "Sí":
					bot.snooze_time(sender_id)
				elif "Sí :)" in texto:
					bot.reading_time(sender_id)
				elif "1 hora" in texto:
					bot.tiempo_lectura(sender_id)
				elif "50 páginas" in texto:
					bot.resumen_diario(sender_id)

		return 'ok' #Este siempre se queda porque le responde un 200 a FB

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar token'

'''@app.route('/notificaciones', method = 'POST')
def notif():
'''
	
if __name__ == "__main__":
	app.run(debug = True)