def palidromo(palavra):
    lista = []

    for i in range(len(palavra)-1, -1 , -1):
        char = palavra[i]
        lista.append(char)

    paralavra_nova = "".join(map(str , lista))

    if paralavra_nova == palavra:
        return 'A palavra inserida e um polídromo'
    else:
        'A palavra inserida não em um polidromo'



print(palidromo(input('Insire uma palavra para saber se ela e um polidromo: ')))
