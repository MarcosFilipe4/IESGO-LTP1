import random

def impar_par():
    return random.randint(1,100)
'''
random é um módulo que fornece funções relacionadas à geração de números 
randint é uma função específica desse módulo. Aqui está o que cada um deles faz:
random: Este é um módulo que oferece várias funções para trabalhar com números aleatórios. Você precisa importar esse módulo usando import random para acessar essas funções.

randint(a, b): Esta é uma função do módulo random que gera um número inteiro aleatório dentro de um intervalo especificado. Os argumentos a e b são os limites inferior e superior do intervalo, respectivamente. O número gerado será maior ou igual a a e menor ou igual a b. Por exemplo, random.randint(1, 6) pode gerar um número aleatório entre 1 e 6, incluindo ambos.

No jogo que eu escrevi no exemplo anterior, a função escolher_numero_aleatorio() usa randint(1, 100) para gerar um número inteiro aleatório entre 1 e 100, que é o número que o computador escolhe secretamente para o jogo.

'''




def principal():
    print('Jogo do Par ou Ímpar!')

    while True:
        numero_eleatorio = impar_par()
        usuario = str(input('Escolha par ou impar: ')).lower()

        if usuario not in ['par' , 'impar']:
            '''
            O operador not in em Python é usado para verificar se um valor não está presente em uma sequência (como uma lista, tupla, string, etc.). Ele retorna True se o valor não estiver na sequência e False
            '''
            print('Invalido, tente novamente com par ou impar')
            continue
            '''
            A palavra-chave continue é usada em loops (como for e while) em Python para controlar o fluxo do programa. Quando o continue é encontrado dentro de um loop, ele faz com que a execução do loop pule para a próxima iteração, ignorando o código restante dentro da iteração atual. Em outras palavras, ele permite que você interrompa a execução do código dentro do loop e vá imediatamente para a próxima iteração do loop
            '''
        usuario_numero = int(input('Escolha um número de 1 a 100: '))

        if usuario_numero < 1 or usuario_numero > 100:
            print('Numero Invalido , Escolha um numero entre 1 a 100')
            continue

        soma = numero_eleatorio + usuario_numero
        resuta = soma %2 == 0

        if (usuario == 'par' and resuta) or (usuario == 'impar' and resuta):
            print('Parabens!  Voce acertou !! O numero eleatorio e ' , numero_eleatorio)
        else:
            print('Voce errou!! Mas tente de novo! . O numero eleatorio era ' , numero_eleatorio)

        nova_tentativa = input('Quer jogar de novo? Sim ou Não').lower()
        if nova_tentativa != 'sim':
            print('Obrigado por jogar meu jogo :D')
            break

principal()


         