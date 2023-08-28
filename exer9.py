def apagar():
    texto = input("Digite uma palavra ")
    return texto.lower().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print(apagar())