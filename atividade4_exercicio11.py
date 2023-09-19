import math
def calcula_esfera(raio):
    volume_esfera = (4/3) * math.pi * (raio ** 3)


def litros_es(litros):
    metros = litros/100
    return metros

raio = float(input('Insira o raio: '))

volume_litro = calcula_esfera(raio)
volume_metros = litros_es(volume_litro)


print('O seu calculo esferico e ' , volume_litro)
print('O valor da sua esfera em litros e ', volume_metros)