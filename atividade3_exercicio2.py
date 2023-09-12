def principal():
    print("Bem-vindo ao Conversor de Moeda!")
    
    moedas = {
        "USD": "Dólar Americano",
        "EUR": "Euro",
        "JPY": "Iene Japonês",
        "AUD": "Dólar Australiano",
       
    }
    
    while True:
        print("\nMoedas disponíveis:")
        for codigo, nome in moedas.items():
            print(f"{codigo} - {nome}")
        
        moeda_origem = input("Digite o código da moeda de origem: ").upper()
        moeda_destino = input("Digite o código da moeda de destino: ").upper()
        
        if moeda_origem not in moedas or moeda_destino not in moedas:
            print("Código de moeda inválido. Certifique-se de usar um código válido.")
            continue
        
        try:
            taxa_cambio = float(input("Digite a taxa de câmbio (1 {moeda_origem} para X {moeda_destino}): "))
            quantidade = float(input(f"Digite a quantidade de {moeda_origem} que deseja converter: "))
        except ValueError:
            print("Valor inválido. Certifique-se de inserir um número válido.")
            continue
        
        resultado = quantidade * taxa_cambio
        print(f"{quantidade} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}")
        
        continuar = input("Deseja fazer outra conversão? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por usar o Conversor de Moeda!")
            break

if __name__ == "__main__":
    principal()
