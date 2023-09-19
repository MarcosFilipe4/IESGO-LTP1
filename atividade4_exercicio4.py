def primo(numero):
    if numero <= 1:
        return False
    if numero <=3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5

    while i * i <= numero:
        if numero % i == 0 or numero (i + 2) == 0:
            return False
        i += 6
    return True
numero = int(input('Digite o numero inteiro: '))

print('Divisores primos deste numero e' , numero)

for divisor in range(1, numero + 1):
    if numero % divisor == 0 and primo(divisor):
        print(divisor)

# Escreva um programa que solicita um número inteiro e exibe todos os seus divisores primos.

'''
Definimos a função eh_primo(numero) para verificar se um número é primo. Esta função usa o algoritmo de verificação de primalidade otimizado.

O usuário é solicitado a inserir um número inteiro usando a função input() e o valor é convertido em um número inteiro com int().

Usamos um loop for que itera de 1 até o número inserido (inclusive).

Dentro do loop, verificamos se cada divisor é primo chamando a função eh_primo(divisor). Se for primo e for um divisor do número inserido, ele é impresso no console.

O programa exibirá todos os divisores primos do número inserido pelo usuário.
'''