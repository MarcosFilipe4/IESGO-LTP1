def signo(dia, mes):
    if (dia >= 21 and mes == 3) or (dia <= 19 and mes == 4):
        return "Áries"
    elif (dia >= 20 and mes == 4) or (dia <= 20 and mes == 5):
        return "Touro"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6): 
        return "Gêmeos"
    elif (dia >= 21 and mes == 6) or (dia <= 22 and mes == 7):
        return "Câncer"
    elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
        return "Leão"
    elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9): 
        return "Virgem"
    elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
        return "Libra"
    elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
        return "Escorpião"
    elif (dia >= 22 and mes == 11) or (dia <= 21 and mes == 12):
        return "Sagitário"
    elif (dia >= 22 and mes == 12) or (dia <= 19 and mes == 1):
        return "Capricórnio"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        return "Aquário"
    elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
        return "Peixes"

ano_atual = 2023
ano = int(input('Digite o seu ano de nascimento: '))
mes = int(input('Digite seu mes de nascimento: '))
dia = int(input('Digite o seu dia de nascimento: '))
idade = ano_atual - ano
print('Sua idade atual e ', idade)
print('E seu signo e ', signo(dia,mes))
