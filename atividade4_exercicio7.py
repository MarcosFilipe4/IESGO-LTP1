numero1 = int(input('Digite um numero inteiro: '))

if numero1 <= 0:
    print('por favor, insira um numero inteiro: ')
else:
    inicial = 0
    for i in range(1, numero1 + 1):
        inicial += i

print('A soma dos valores entre 1 e ' , numero1 , ' e ' , inicial )