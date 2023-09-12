def verificador(jogador1, jogador2):
    

    if jogador1 == jogador2:
        return "Empate"
    elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
         (jogador1 == "papel" and jogador2 == "pedra") or \
         (jogador1 == "tesoura" and jogador2 == "papel"):
        return "Jogador 1 vence!"
    else:
        return "Jogador 2 vence!"

def principal():
    print("Bem-vindo ao jogo Pedra, Papel e Tesoura!")

    while True:
        jogador1 = input("Jogador 1, escolha pedra, papel ou tesoura: ").lower()
        jogador2 = input("Jogador 2, escolha pedra, papel ou tesoura: ").lower()

        if jogador1 not in ["pedra", "papel", "tesoura"] or jogador2 not in ["pedra", "papel", "tesoura"]:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue

        print(f"Jogador 1 escolheu {jogador1}. Jogador 2 escolheu {jogador2}.")

        resultado = verificador(jogador1, jogador2)
        print(resultado)

        jogar_novamente = input("Deseja jogar novamente? ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    principal()
