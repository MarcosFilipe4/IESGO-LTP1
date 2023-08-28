# Exercício 06 - Crie uma aplicação que solicite ao usuário digitar o seu nome e sobrenome e imprima no console o nome com todas as letras maiúsculas e o sobrenome com todas as letras minúsculas sem espaços entre o nome e o sobrenome e sem alterar a variável original.
def nome_e_sobrenome():
    nome = input('Insira seu nome completo')
    parte_nome = nome.split()
    primeiro_nome = parte_nome[0]
    segundo_nome = " ".join(parte_nome[1:])

    return primeiro_nome.upper() + " " + segundo_nome.lower()

print(nome_e_sobrenome())
