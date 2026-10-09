from flask import Flask, jsonify, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    titulo = request.form['titulo']
    tarefa = {
        "id": max([t['id'] for t in tarefas], default=0) + 1,
        "titulo": titulo,
        "descricao": "",
        "concluida": False
    }
    tarefas.append(tarefa)
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    return redirect('/')

@app.route('/concluir/<int:tarefa_id>')
def concluir_tarefa(tarefa_id):
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            break
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    return redirect('/')

@app.route('/excluir/<int:tarefa_id>')
def excluir_tarefa(tarefa_id):
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)

    tarefas = [t for t in tarefas if t['id'] != tarefa_id]
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    return redirect('/')

@app.route('/tarefas')
def listar_tarefas():
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
    return jsonify(tarefas)

if __name__ == '__main__':
    app.run(debug=True)

