## Exercício 9 - Escreva um programa que solicita ao usuário as dimensões de um retângulo e o programa retorna o perímetro e a área do retângulo.

def calcula_retangulo():
    comprimento_retangulo = float(input('Digite o comprimento do seu retângulo: '))
    largura_retangulo = float(input('Digite a largura do seu retângulo: '))
    area_retangulo = comprimento_retangulo*largura_retangulo
    perimetro_retangulo = 2 * (comprimento_retangulo+largura_retangulo)

    print('A área do retângulo é ' , area_retangulo)
    print('Ja o se perímetro do retângulo é: ' , perimetro_retangulo)


calcula_retangulo()
