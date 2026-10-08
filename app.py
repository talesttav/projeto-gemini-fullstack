tarefas = []

def adicionar_tarefa(titulo, descricao):
    novo_id = len(tarefas) + 1
    nova_tarefa = {
        'id': novo_id,
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(nova_tarefa) 


def concluir_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['concluida'] = True
            print(f"Tarefa ID: {tarefa_id} concluída com sucesso!")
            return




def listar_tarefas():
        for tarefa in tarefas:
            print(f"Tarefa ID: 0{tarefa['id']}, \nTítulo: {tarefa['titulo']}\n")

adicionar_tarefa("Estudar Python", "Criar a primeira estrutura em memória")
adicionar_tarefa("Configurar Git", "Iniciar repositório do projeto") 

listar_tarefas()

concluir_tarefa(1)