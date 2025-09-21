# Luan Ferreira
import random
from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    "A única maneira de fazer um ótimo trabalho é amar o que você faz. - Steve Jobs",
    "A persistência é o caminho do êxito. - Charles Chaplin",
    "O sucesso é a soma de pequenos esforços repetidos dia após dia. - Robert Collier",
    "A imaginação é mais importante que o conhecimento. - Albert Einstein",
    "Se você quer viver uma vida feliz, amarre-se a um objetivo, não às pessoas ou às coisas. - Albert Einstein"
]

@app.route("/")
def home():
    return "<h1>API de Citações</h1><p>Para obter uma citação aleatória, acesse a rota /quote</p>"

@app.route("/quote")
def get_quote():
    random_quote = random.choice(quotes)
    return jsonify({"citacao": random_quote})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)