def calcula(n):
    fibonacci = [0 , 1]

    while len(fibonacci) < n:
        priximo_n = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(priximo_n)

    return fibonacci

try:
     n = int(input('quantos numeros fibonacci voce deseja' ))
except ValueError:
    print('insira um numero inteiro, Por favor!')
    exit()

if n <= 0:
    print('insira um valor inteiro positivo')
else: 
    numero_usuario_fibocanni = calcula(n)

    print('Os numeros são:')
    print(",".join(map(str, numero_usuario_fibocanni)))