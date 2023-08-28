def letras_contas(letra):
    frase_docliente = input('Digite seu nome Completo ').lower() #aqui eu criei um input em que o usuario digita seu nome completo e o lower transforma todo o nome em minuscula
    return  frase_docliente.count(letra)

contar_a = 'a' # aqui eu coloquei a letra que eu quero contar
print('O nome inserido contem ' , letras_contas(contar_a), 'quantidades de letras ' , contar_a)