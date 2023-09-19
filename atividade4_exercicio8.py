numero1 = int(input('Digite um numero inteiro: '))

if numero1 <= 0:
    print('por favor, insira um numero inteiro: ')
else:
    inicial = 0
    for i in range(1, numero1 + 1):
        if i % 3 == 0 or i % 5 == 0:
            inicial += i
            print(inicial)