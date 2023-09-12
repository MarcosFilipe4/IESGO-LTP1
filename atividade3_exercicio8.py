import random

def jogo_de_adivinhacao():
    # Gere um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    
    tentativas_acertos = 0
    maximas_tentativas = 10  # Você pode ajustar o número de tentativas aqui

    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Tente adivinhar o número entre 1 e 100. Você tem {maximas_tentativas} tentativas.")

    while tentativas_acertos < maximas_tentativas:
        try:
           
            palpite = int(input("Digite  o palpite: "))

            
            if palpite == numero_secreto:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas_acertos+1} tentativas.")
                break
            elif palpite < numero_secreto:
                print("O número é maior. Tente de novo.")
            else:
                print("O número é menor. Tente de novo.")

            tentativas_acertos += 1

        except ValueError:
            print("Por favor, insira um número válido.")

    if tentativas_acertos == maximas_tentativas:
        print(f"Suas {maximas_tentativas} tentativas acabaram. número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_de_adivinhacao()
