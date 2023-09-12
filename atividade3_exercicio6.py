
def tem():
    usuario = int(input('escolha 1 para Cº a Fº ou 2 para Fº a Cº:  '))
    temperatura = float(input('Insira sua temperatura: '))
    casas_decimais = int(input('quantas casas decimais? '))
#aqui são todos os inputs de resposta do usuario

    if usuario == 1:
        resultado = (temperatura * 1.8) + 32
        formatado = "{:.{}f}".format(resultado,casas_decimais) #aqui eu faço com o usuario formate e coloque quantas casas decimais ele vai querer
        print('Seu resultado e ' ,formatado)
       
    elif usuario == 2:
        resultado1 = (temperatura - 32)/1.8
        formatado1 = "{:.{}f}".format(resultado1,casas_decimais)
        print('Seu resultado e ', formatado1)
        
    else:
        print('Opção invalida')
        tem()


tem()