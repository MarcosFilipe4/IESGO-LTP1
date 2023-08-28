def aumenta_nome():
    texto = input('Digite seu nome completo para o transforma em maiúscula:')
    aumenta = texto.upper() #tag upper(função de colocar todas as letras inseridas em maiusculas)
    return aumenta

nome = aumenta_nome()
print('Seu nome e ', nome)