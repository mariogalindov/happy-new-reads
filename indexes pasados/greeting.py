greeting.py

#app.py
def greeting():
	if request.method =="POST":
		bot.greeting()

#responses.py

	def greeting(self):
		JSON = {
			"get_started":{
    			"payload":"<Hola>"
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
		return True