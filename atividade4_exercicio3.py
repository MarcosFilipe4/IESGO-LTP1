numero1 = int(input('Digite um numero para saber os seus divisores: '))


for divisor in range(1, numero1 + 1):
    if numero1 % divisor == 0:
        print(divisor)

#Escreva um programa que solicita um número inteiro e exibe todos os seus divisores.