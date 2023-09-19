import random

numero_da_sorte = random.randint(1,9)

tentativas = 0

print('Bem vindo!')

while True:
    tentativas = int(input('Advinha o numero entre 1 a 9: '))
    tentativas += 1

    if tentativas == numero_da_sorte:
        print('Parabens, voce adivinhou o numero')
    elif tentativas < numero_da_sorte:
        print('Errou! mas o numero sorteado e maior')
    else:
        print('Errou ! mas o numero sorteado menor! ')