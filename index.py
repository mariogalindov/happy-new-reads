#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from responses import Responses

app = Flask(__name__)

ACCESS_TOKEN = 'EAAEzHJeqzxsBABisf2HpZCD4EdudErzscxGQDHENCEFhJMkCxun8bT00w0BpZCukLDwwZCQGGbcEqp9QAJmaorp93HXb6Tl3HxNlR9wcbQVn37Eu5FM3Oft51gQnD4pZCl69dPD1hNobEcODokyw48subgkD0nFa1Bs4TwV9cgZDZD'
VERIFY_TOKEN = 'one5udx4'

@app.route("/")
def index():
	return "Bot iniciado"

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
		

if __name__ == "__main__":
	app.run(debug = True)