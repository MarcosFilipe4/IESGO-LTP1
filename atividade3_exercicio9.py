def imc(peso,altura):
    imc = peso/(altura**2)
    return imc

def verifica(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif  18.5 <= imc <24.9:
        return 'Dentro do peso Ideal'
    elif 24.9 <= imc <29.9:
        return 'Acima do peso'
    else:
        return 'Obeso'
    

peso = float(input('Insira seu peso em kg: '))
altura = float(input('Digite sua aaltura (em metros): '))

resultado = imc(peso,altura)

print('Seu imc e ', resultado)
print('Seu status de saude e ',verifica(resultado) )