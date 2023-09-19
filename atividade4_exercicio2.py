numero1  = int(input('Digite um numero inteiro: '))
numero2 = int(input('Digite outro numero inteiro: '))

for numero1 in range(numero1,numero2):
    #numero1 inicia e vai ate o numero2
    #ja em baixo o if ve se o numero e divisivel por e sobre 0 e ai sim imprime todos os valores pares
    
    if numero1%2 == 0:
        print(numero1)

#Escreva um programa que solicita dois números inteirtos (sendo o primeiro o limite inferior e o segundo o limite superior) e exibe todos os números pares entre esses limites.
