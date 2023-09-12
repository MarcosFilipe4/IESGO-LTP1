import csv

def carregar_agenda():
    try:
        with open("agenda.csv", mode="r", newline="") as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)
            return [contato for contato in leitor_csv]
    except FileNotFoundError:
        return []

def salvar(agenda):
    with open("agenda.csv", mode="w", newline="") as arquivo_csv:
        campos = ["nome", "telefone"]
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor_csv.writeheader()
        escritor_csv.writerows(agenda)

def adicionar(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    contato = {"nome": nome, "telefone": telefone}
    agenda.append(contato)
    print(f"Contato '{nome}' adicionado com sucesso!")

def pesquisa(agenda):
    termo = input("Digite o nome do contato que deseja pesquisar: ")
    resultados = [contato for contato in agenda if termo.lower() in contato["nome"].lower()]
    
    if not resultados:
        print("Nenhum contato encontrado com esse nome.")
    else:
        print("Contatos encontrados:")
        for contato in resultados:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def editar(agenda):
    nome = input("Digite o nome do contato que deseja editar: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
            novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
            
            if novo_nome:
                contato["nome"] = novo_nome
            if novo_telefone:
                contato["telefone"] = novo_telefone
            
            print("Contato editado com sucesso!")
            return
    
    print("Contato não encontrado.")

def excluir(agenda):
    nome = input("Digite o nome do contato que deseja excluir: ")
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            print("Contato excluído com sucesso!")
            return
    
    print("Contato não encontrado.")

def principal():
    agenda = carregar_agenda()
    
    while True:
        print("\nOpções disponíveis:")
        print("1. Adicionar contato")
        print("2. Pesquisar contato")
        print("3. Editar contato")
        print("4. Excluir contato")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            adicionar(agenda)
        elif escolha == "2":
            pesquisa(agenda)
        elif escolha == "3":
            editar(agenda)
        elif escolha == "4":
            excluir(agenda)
        elif escolha == "5":
            salvar(agenda)
            print("Agenda salva. Obrigado por usar a agenda telefônica!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__principal__":
    principal()

'''
Importamos o módulo csv para lidar com a leitura e gravação de arquivos CSV

Função carrega

Esta função é responsável por carregar a agenda telefônica a partir do arquivo "agenda.csv" (se ele existir). Ela lê o arquivo CSV e retorna uma lista de dicionários, onde cada dicionário representa um contato com as chaves
"nome" e "telefone". Se o arquivo não for encontrado (primeira vez que o programa é executado), ela retorna uma lista vazia.

Função salva

Esta função é responsável por salvar a agenda telefônica no arquivo "agenda.csv". Ela recebe a lista de contatos como argumento e escreve os dados no arquivo CSV. Primeiro, escreve a linha de cabeçalho
com os nomes das colunas ("nome" e "telefone") e, em seguida, escreve os contatos um por um no arquivo.

Função adiciona

Esta função permite ao usuário adicionar um novo contato à agenda. Ela solicita o nome e o telefone do contato ao usuário, cria um dicionário
representando o contato e o adiciona à lista de contatos. Em seguida, exibe uma mensagem de confirmação.

Função pesquisar

Esta função permite ao usuário pesquisar contatos na agenda pelo nome. Ela solicita um termo de pesquisa e verifica se esse termo está contido no nome de algum contato (ignorando maiúsculas/minúsculas).
Se encontrar contatos correspondentes, os exibe; caso contrário, exibe uma mensagem de "Nenhum contato encontrado".

Função editar

Esta função permite ao usuário editar um contato existente na agenda. O usuário fornece o nome do contato que deseja editar. Se o contato é encontrado, o usuário pode fornecer um novo nome e/ou um novo telefone. Os dados do contato são atualizados, e uma mensagem
de confirmação é exibida. Se o contato não for encontrado, uma mensagem de "Contato não encontrado" é exibida.

Função excluir

Esta função permite ao usuário excluir um contato existente na agenda. O usuário fornece o nome do contato que deseja excluir. Se o contato é encontrado, ele é removido da lista de contatos,
e uma mensagem de confirmação é exibida. Se o contato não for encontrado, uma mensagem de "Contato não encontrado" é exibida.

Função principal 

Esta função é a função principal do programa. Ela cria uma lista agenda carregando os contatos existentes do arquivo CSV. Em seguida, entra em um loop que exibe um menu de opções
e permite ao usuário escolher o que fazer. As opções incluem adicionar, pesquisar, editar, excluir contatos ou sair do programa.

Chamada if __name__ == "__principal__":
Esta linha verifica se o código está sendo executado como um programa principal 

'''
