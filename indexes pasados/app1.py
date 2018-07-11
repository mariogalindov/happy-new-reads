#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from responses import Responses

app = Flask(__name__)

ACCESS_TOKEN = 'EAAKHni1byYIBAKp0ew5xQpoQdX6S3ZCqf2MHnyzMyE4IDeSW0MyQql51LnEY4NxsF3sLkmQEJtgNEyNBmkq5nusFRJZAxHG9mn7UNYpBaw4FfiV89CYtkSCQEYCAhmHXup9yKfC8dfHWZClZAOoHcZAtoIvlSuKAHVZCP18LwThhTM9Ymazgwa'
VERIFY_TOKEN = 'one5udx4'

bot = Responses(ACCESS_TOKEN)


@app.route("/")
def index():
	return "Bot iniciado"

@app.route('/webhook', methods = ['GET', 'POST'])

def greeting():
	if request.method == 'POST':
		bot.greeting(self)




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
				elif texto == "75 páginas":
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