def fatorial(numero):
    if numero < 0:
        return 'ERROR numero negativo!'
    elif numero == 0:
        return 1
    else:
        resuta = 1
    for i in range(1, numero + 1):
        resuta *= i
    return resuta

numero = int(input('Digite um numero inteiro para saber seu fatorial: '))

resultado = fatorial(numero)

print(resultado)


    