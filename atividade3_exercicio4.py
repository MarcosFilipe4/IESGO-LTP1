def contador(frase):
    formatado = frase.upper().replace("","")
    divide = frase.split()
    numero_palavra = len(divide)
    #no return eu dei dois parametros para o numero de palavras e a palavra formatada.(Assim quando eu for chamar a função, eu colocar estes dois parametros de return)
    return numero_palavra,formatado



frase = input('Insire a frase: ')

resultado_palavra,resultado_formata = contador(frase)

print('O numero de palavras na frase é: ', resultado_palavra)
print('A sua frase formatada e : ' , resultado_formata)
