from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    return render_template('index.html', tarefas=tarefas)

@app.route('/tarefas')
def listar_tarefas():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)

