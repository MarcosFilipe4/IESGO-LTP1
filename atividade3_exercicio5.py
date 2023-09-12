import os

# Função para carregar a lista de tarefas a partir de um arquivo
def carregador_tarefa():
    if os.path.exists("tarefas.txt"):
        with open("tarefas.txt", "r") as arquivo:
            tarefa = arquivo.readlines()
        return [tarefa.strip() for tarefa in tarefa]
    else:
        return []

# Função para salvar a lista de tarefas em um arquivo
def salvador_tarefa(tarefa):
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefa:
            arquivo.write(tarefa + "\n")

# Função para mostrar a lista de tarefas
def mostrar_tarefa(tarefas):
    if not tarefas:
        print("Lista vazia.")
    else:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa(tarefas, tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada à lista.")

# Função para marcar uma tarefa como concluída
def marcar_como_concluida(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa = tarefas[indice - 1]
        tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa}' marcada como concluída.")
    else:
        print("inválido")

# Função para remover uma tarefa da lista
def remover_tarefa(tarefas, indice):
    if 1 <= indice <= len(tarefas):
        tarefa = tarefas[indice - 1]
        tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa}' removida da lista.")
    else:
        print("inválido.")


def principal():
    tarefas = carregador_tarefa()


    while True:
        print('\nOpções:')
        print('1. Suas Tarefas')
        print('2. Adicionar tarefas')
        print('3. Marcar como concluido')
        print('4. Remova sua tarefa')
        print('5. Sair')

        opcao = input('Escolha uma opção')

        if opcao == '1':
            mostrar_tarefa(tarefas)
        elif opcao == '2':
            tarefa_nova = input('Digite sua nova tarefa: ')
            adicionar_tarefa(tarefas,tarefa_nova)
        elif opcao == '3':
            mostrar_tarefa(tarefas)
            indice = int(input('Digite a tarefa concluida: '))
            marcar_como_concluida(tarefas,indice)
        elif opcao == '4':
            mostrar_tarefa(tarefas)
            indice = int(input('Digite as tarefa que sera removida: '))
            remover_tarefa(tarefas,indice)
        elif opcao == '5':
            salvador_tarefa(tarefas)
            print('Saindo.... ')
            break
        else:
            print('Opção invalida.')

if __name__ == "__main__":
    principal()