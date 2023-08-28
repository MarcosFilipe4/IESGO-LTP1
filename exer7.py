#7 - Crie uma aplicação em que o usuário digite o seu nome e sobrenome de uma só vez e armazene o nome em uma variável 'nome_usuário' e o sobrenome em uma variável 'sobrenome_usuario'. Em seguida, crie uma variável 'nome_completo' que armazene o nome completo do usuário com todas as letras maiúsculas e imprima no console o nome completo do usuário com todas as letras minúsculas. Além disso, crie outra variável chamada 'tamanho_nome_completo' que armazene o tamanho do nome completo do usuário e imprima no console o tamanho do nome completo do usuário.
def digita_nome(nome):
    
    partedo_nome = nome.split()
    nomedo_usuario = partedo_nome[0]
    sobrenomedo_usuario = " ".join(partedo_nome[1:])  # join e utilizado para combinar uma sequencia em uma única string, como uma lista ou conjunto.
    nome_completo = nome.upper()
    tamanho_completo_nome = len(nome)

    print('Nome: ' , nome_completo.lower())
    print('tem ', tamanho_completo_nome , 'quantidades de caracteres')

digita_nome(input('Digite seu nome completo (evite espaços)!'))