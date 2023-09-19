def nome(texto, nome):
    contador = 0

    texto = texto.lower()
    nome= nome_usuario.lower()

    for letra in texto:
        if letra in nome:
            contador +=1

    return contador

usuario = input('Digite um texto: ')

nome_usuario = "SeuNome"

resulta = nome(usuario, nome_usuario)

print('O numero de letras do seu nome no texto que foi inserido é ' , resulta)
