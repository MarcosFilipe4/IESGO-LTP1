def vogais(): 
    frase = input("Digite uma palavra ") #aqui eu coloquei o input de pergunta para o usuario
    return frase.lower().replace('a', '*').replace('e', '*').replace('i', '*').replace('o', '*').replace('u', '*')

print(vogais())