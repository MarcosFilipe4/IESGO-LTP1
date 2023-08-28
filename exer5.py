def diminui_nome():
    texto = input('Insira seu nome completo maiuscula para o transformar em minuscula: ')
    diminui = texto.lower()
    return diminui

nome = diminui_nome()

print('Seu nome e ' , nome)