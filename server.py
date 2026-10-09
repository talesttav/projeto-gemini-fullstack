from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Meu primeiro servidor Web está funcionando!</h1>"

@app.route('/tarefas')
def listar_tarefas():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)

