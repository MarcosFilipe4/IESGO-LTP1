def calcula_quadrados(numero):
    quadrados = {}
    for i in range(1, numero + 1):
        quadrados[i] = i * i
    return quadrados

def principal():
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n < 1:
            print("Por favor, insira um número inteiro positivo.")
        else:
            quadrados = calcula_quadrados(n)
            print("Quadrados dos números de 1 a", n, ":")
            for i, quadrado in quadrados.items():
                print(i, ":", quadrado)
    except ValueError:
        print("Entrada inválida.")

if __name__ == "__main__":
    principal()
