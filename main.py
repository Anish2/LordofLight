from flask import Flask
from flask import request
from flask import jsonify

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot(
    'Kubera',
    read_only=True
)

chatbot.set_trainer(ChatterBotCorpusTrainer)

chatbot.train(
    "./botprofile.corpus.json"
)

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file('coffee.html')

@app.route("/chat", methods=['GET'])
def chat():
    return app.send_static_file('chat.html')

@app.route("/chat", methods=['POST'])
def respond():
    message = request.form['message']
    return chatbot.get_response(message).text

if __name__ == "__main__":
    app.run(debug=True)