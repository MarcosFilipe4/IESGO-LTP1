import string

def analisador_de_string(string_ip):
    #aqui estou iniciando meus contadores
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0
    palavras = len(string_ip.split())

    for char in string_ip:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1
        elif char.isdigit():
            digitos += 1
        elif char in string_ip.punctuation:
            especiais += 1

        
    return maiusculas,minusculas,digitos,especiais,palavras
    

usuario = input('Digite a string: ')

maiusculas, minusculas, digitos, especiais, palavras = analisador_de_string(usuario)

print('Letras miusculas: ' , maiusculas)
print('Letras minusculas' , minusculas)
print('Digitos :' , digitos)
print('Caracteres especiais: ' , especiais)
print('Palavras: ' , palavras)

