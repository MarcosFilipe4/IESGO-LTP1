from datetime import datetime

def calcular_idade_em_meses(data_nascimento, data_atual):
    anos = data_atual.year - data_nascimento.year
    meses = data_atual.month - data_nascimento.month
    if data_atual.day < data_nascimento.day:
        meses -= 1
    return anos * 12 + meses

def calcular_idade_em_dias(data_nascimento, data_atual):
    delta = data_atual - data_nascimento
    return delta.days

def calcular_idade_em_horas(data_nascimento, data_atual):
    delta = data_atual - data_nascimento
    return delta.days * 24

def calcular_idade_em_minutos(data_nascimento, data_atual):
    delta = data_atual - data_nascimento
    return delta.days * 24 * 60

def calcular_idade_em_segundos(data_nascimento, data_atual):
    delta = data_atual - data_nascimento
    return delta.days * 24 * 60 * 60

def obter_data_input(mensagem):
    data_str = input(mensagem)
    return datetime.strptime(data_str, "%Y-%m-%d")

def exibir_menu():
    print("Selecione uma opção:")
    print("1. Calcular idade em meses")
    print("2. Calcular idade em dias")
    print("3. Calcular idade em horas")
    print("4. Calcular idade em minutos")
    print("5. Calcular idade em segundos")
    print("6. Sair do programa")

def main():
    data_nascimento = obter_data_input("Digite a sua data de nascimento (YYYY-MM-DD): ")
    data_atual = datetime.now()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1/2/3/4/5/6): ")

        if escolha == "1":
            idade_em_meses = calcular_idade_em_meses(data_nascimento, data_atual)
            print(f"Sua idade em meses é: {idade_em_meses} meses")
        elif escolha == "2":
            idade_em_dias = calcular_idade_em_dias(data_nascimento, data_atual)
            print(f"Sua idade em dias é: {idade_em_dias} dias")
        elif escolha == "3":
            idade_em_horas = calcular_idade_em_horas(data_nascimento, data_atual)
            print(f"Sua idade em horas é: {idade_em_horas} horas")
        elif escolha == "4":
            idade_em_minutos = calcular_idade_em_minutos(data_nascimento, data_atual)
            print(f"Sua idade em minutos é: {idade_em_minutos} minutos")
        elif escolha == "5":
            idade_em_segundos = calcular_idade_em_segundos(data_nascimento, data_atual)
            print(f"Sua idade em segundos é: {idade_em_segundos} segundos")
        elif escolha == "6":
            print("Obrigado por usar o programa!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
