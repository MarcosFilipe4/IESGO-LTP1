import random

def gerar_numero_cartao(empresa):
    # Dicionário de prefixos de números de cartão de crédito fictícios para diferentes empresas
    prefixos = {
        'Visa': '4',
        'MasterCard': '5',
        'Discover': '6',
        'Elo' : '6'
    }

    if empresa not in prefixos:
        print("Empresa de cartão de crédito não suportada.")
        return

    
    prefixo = prefixos[empresa]
    numero_aleatorio = ''.join(random.choice('0123456789') for _ in range(14))
    numero_cartao = prefixo + numero_aleatorio

    
    soma = 0
    multiplica_por_dois = False

    for digito in reversed(numero_cartao):
        d = int(digito)
        if multiplica_por_dois:
            d *= 2
            if d > 9:
                d -= 9
        soma += d
        multiplica_por_dois = not multiplica_por_dois

    digito_verificacao = (10 - (soma % 10)) % 10
    numero_cartao += str(digito_verificacao)

    return numero_cartao


empresa = str(input('Digite bandeira do cartão\n Visa \n MasterCard \n Discover \n Elo \n Bandeira:  '))
numero_gerado = gerar_numero_cartao(empresa)
print(f"Número do cartão de crédito ({empresa}): {numero_gerado}")
