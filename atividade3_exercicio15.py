import random

def gerador_de_sim_nao():
    resposta = ['Sim' , 'Não' , 'Talvez']
    return random.choice(resposta)


def principal():
    pergunta_usuario = str(input('Digite sua pergunta: '))
    resposta = gerador_de_sim_nao()
    print(pergunta_usuario , resposta)


principal()