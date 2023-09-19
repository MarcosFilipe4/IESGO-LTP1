def calcula_raiz(n):
    if n < 0:
        return 'O numero não e positivo!'
    
    raiz_aproxima = n

    precisao = 0.001

    while True:
        nova_aproximação = 0.5*(raiz_aproxima + n/raiz_aproxima)

        if abs(nova_aproximação - raiz_aproxima) < precisao:
            break
        raiz_aproxima = nova_aproximação

    return nova_aproximação

while True:
    try:
        numero = int(input('Digite um numero inteiro positivo: '))
        if numero > 0:
            break
        else:
            print('O numero deve ser positivo. ')
    except ValueError:
        print('Invalida')

raiz = calcula_raiz(numero)

print('A raiz quadrada de ' , numero , 'com a precisão de 0.001 é aproximadamente' ,raiz)