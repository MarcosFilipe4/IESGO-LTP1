import random
import string

def geradorde_senha(comprimento, letra=4, numero=4, especiais=2):
    if comprimento < (letra + numero + especiais):
        print('Comprimento mínimo não atendido.')
        return None

    aleatorias_letras = ''.join(random.choice(string.ascii_letters) for _ in range(letra))
    #meu gerador de letras aleatórias

    aleatorio_numero = ''.join(random.choice(string.digits) for _ in range(numero))
    #meu gerador de numeros aleatorios

    aleatorio_especiais = ''.join(random.choice(string.punctuation) for _ in range(especiais))
    #meu geradir de caracteres especias eleatório

    resto = comprimento - (letra + numero + especiais)
    caracteres = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(resto))

    senhado_usuario = aleatorias_letras + aleatorio_especiais + aleatorio_numero + caracteres
    senha_resultado = ''.join(random.sample(senhado_usuario,len(senhado_usuario)))

    return senha_resultado

comprimento_senha = int(input('qual o comprimento da senha desejado: '))

letra = int(input('Quantas letras a senha deve ter? '))
numero = int(input('Quantos numero a senha deve conter? '))
especiais = int(input('Quantos caracteres especiais a senha deve conter?: '))

senha_gerada_usuario = geradorde_senha(comprimento_senha,letra,numero,especiais)

print('Senha gerada: ' , senha_gerada_usuario)

  