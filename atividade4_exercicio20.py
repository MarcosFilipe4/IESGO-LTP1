def principal():
    
    texto = input("Digite uma string longa: ")

    # Dividir a string em palavras
    palavras = texto.split()

    # Inicializar listas vazias para cada critério
    comeca_com_maiuscula = []
    termina_com_vogal = []
    mais_de_5_letras = []
    inverso_palavras = []

    # Iterar sobre cada palavra na lista de palavras
    for palavra in palavras:
        # Verificar se a palavra começa com letra maiúscula
        if palavra[0].isupper():
            comeca_com_maiuscula.append(palavra)

        # Verificar se a palavra termina com vogal
        if palavra[-1].lower() in 'aeiou':
            termina_com_vogal.append(palavra)

        # Verificar se a palavra tem mais de 5 letras
        if len(palavra) > 5:
            mais_de_5_letras.append(palavra)

        # Inverter a palavra manualmente
        palavra_invertida = ''.join(reversed(palavra))
        inverso_palavras.append(palavra_invertida)

    # Imprimir os resultados
    print("Palavras com letra maiúscula:", ' '.join(comeca_com_maiuscula))
    print("Palavras que terminam com vogal:", ' '.join(termina_com_vogal))
    print("Palavras com mais de 5 letras:", ' '.join(mais_de_5_letras))
    print("Inverso de cada palavra na string original:", ' '.join(inverso_palavras))

if __name__ == "__main__":
    principal()
