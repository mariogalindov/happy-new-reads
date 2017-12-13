#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from responses import Responses

app = Flask(__name__)

ACCESS_TOKEN = 'EAAKHni1byYIBAOFXGbTIOmUGb59kK20zSNsZAiPYegFxV8YHTcaT43NXNPgVWeiCON7N6aE7BN4Q6mZBznBMoajFsi2g0k7GDXuiGqh6a45cTMF940CKhbLvfbXHPfj1v4VPA2i9NHzaiPazaFZATz688tOziWnfiUjo2qZBFAZDZD'
VERIFY_TOKEN = 'one5udx4'

bot = Responses(ACCESS_TOKEN)


@app.route("/")
def index():
	return "Bot iniciado"

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		message = request.json
		for event in message["entry"]:
			messaging = event["messaging"]
			for event_message in messaging:
				sender_id = event_message["sender"]["id"]
		bot.saluda(sender_id)
		return 'ok' #Este siempre se queda porque le responde un 200 a FB



	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar token'
		

if __name__ == "__main__":
	app.run(debug = True)