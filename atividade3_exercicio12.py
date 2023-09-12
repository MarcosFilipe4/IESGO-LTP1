def imprimir_(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verifica(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

def principal():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    vitorias_X = 0
    vitorias_O = 0

    while True:
        imprimir_(tabuleiro)
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha 0 1 2 : "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna 0 1 2 : "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verifica(tabuleiro, jogador_atual):
                imprimir_(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                if jogador_atual == "X":
                    vitorias_X += 1
                else:
                    vitorias_O += 1
                print(f"Placar: Jogador X - {vitorias_X}, Jogador O - {vitorias_O}")
                jogar_novamente = input("Deseja jogar de novo? (s/n): ").lower()
                if jogar_novamente == "s":
                    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
                else:
                    break
            else:
                jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição ocupada. Tente novamente.")

if __name__ == "__main__":
    principal()


