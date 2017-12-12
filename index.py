from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Bot iniciado"

@app.route('/webhook', methods = ['GET', 'POST'])
def webhook():
	if request.method == 'POST':
		message = request.json
		print(message)

		for event in message["entry"]:
			messaging = event["messaging"]
			for event_message in messaging:
				sender_id = event_message["sender"]["id"]

				'''	
					validar si es un mensaje o un payload 

				'''
				replies = Respuestas()

				message = event_message["message"]["text"]
				
				if message == "SALUDO":
					#BOT SALUDA
					replies.saluda(sender_id)

				elif message == "HORA":
					#BOT ALKSDHJKASD

				if payloda == "220":
					#bot say number page 

		return "ok"

	elif request.method == 'GET':
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		return 'Verificar token'	

if __name__ == "__main__":
	app.run(debug = True)