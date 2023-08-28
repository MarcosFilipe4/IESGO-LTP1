#Exercício 08 - Crie um programa que solicite apresenta um menu de opções no Console e solicite ao usuário que digite a opção desejada. Em seguida, crie uma função para cada opção do menu que execute a ação solicitada pelo usuário. O menu deve conter as seguintes opções:
"""
1. Conte o número total de palavras digitadas.
2. Conte o número de vogais na palavra digitada (ignore maiúsculas/minúsculas, ou seja, "Python" e "python" devem ser contadas como iguais).
3. Substitua todas as ocorrências da palavra "Python" por "Java".
4. Converta todas as letras da string para minúsculas.
5. Crie uma lista com todas as palavras únicas encontradas na string (ignorando maiúsculas/minúsculas).
6. Imprima as palavras na string em ordem alfabética.
"""
def menu_selecao(selecionado):
    if selecionado >=1 or selecionado <=6:
        texto = input("\nDigite a palavra ou frase: ")
  
    if selecionado == 1:
        print("Opção selecionada: 1")
        print(caracteres_conta(texto),"\n")
            
    elif selecionado == 2:
        print("Opção selecionada: 2")
        print(vogais(texto),"\n")
    
    elif selecionado == 3:
        print("Opção selecionada: 2")
        print(funcao_substituir_txt(texto),"\n")
    
    elif selecionado == 4:
        print("Opção selecionada: 4")
        print(diminui_nome(texto),"\n")
        
    elif selecionado == 5:
        print("Opção selecionada: 5")
        print(lista_unica_pala(texto))
        
    elif selecionado == 6:
        print("Opção selecionada: 6")
        print(alfabetica(texto))
    else:
        print('Opção não indentificada! \nDigite um numero correto!')


def voltamenu(texto):
    if texto == "sim" or "SIM":
        return menu()
    else:
        print("Obrigado por usar meu sistema :D")
    

def caracteres_conta(texto):
    quantidade_de_pala = texto.split()
    if len(quantidade_de_pala) > 1:
        return f"O texto Digitado contém {len(quantidade_de_pala)} palavras "
    else:
        return f"{len(quantidade_de_pala)} palavra Digitada "
    


def vogais(texto): 
    quantidade = texto.count('a')+texto.count('e')+texto.count('i')+texto.count('o')+texto.count('u')
    if quantidade > 1:
        return f"Testo Digitado contem {quantidade} vogais"
    else:
        return f"Texto Digitado contem {quantidade} vogais"


def funcao_substituir_txt(texto):
    troca_frase = texto.lower().replace('python','java')
    return f"trocou: \n{troca_frase}"


def diminui_nome(texto):
    diminui = texto.lower()
    return diminui

def lista_unica_pala(texto):
    texto = texto.lower().split()
    palavra = list(set(texto))
    return f"Palavras em ordem alfabetica: \n{palavra}"

def alfabetica(texto):
    palavras_list = texto.split() 
    palavras_list = sorted(palavras_list)
    return f"Palavra em ordem alfabetica: \n{palavras_list}"

def menu(): #aqui eu criei a função do menu do meu sistema com todas as opções 
    
    opcao1 = " 1. Conte o número total de palavras digitadas."
    opcao2 = "2. Conte o número de vogais na palavra digitada "
    opcao3 = "3. Substitua todas as ocorrências da palavra Python por Java."
    opcao4 = "4. Converta todas as letras da string para minúsculas."
    opcao5 = "5. Crie uma lista com todas as palavras únicas encontradas na string."
    opcao6 = "6. Imprima as palavras na string em ordem alfabética."
    print("BEM VINDO AO MEU SISTEMA  :D")
    print("MENU DE OPÇÕES: ")
    print(f"{opcao1}\n {opcao2}\n{opcao3}\n{opcao4}\n{opcao5}\n{opcao6}\n") #exibe o meu menu , conectando todas as minhas opções acima
    selecionado = input("Digite a opção desejada: ")
    menu_selecao(int(selecionado)) #variavel com o resultado do cliente (numero que meu cliente escolheu)
    volta = voltamenu(input("Deseja voltar ao menu? sim ou não: " )) #aqui eu fiz uma função para que ao meu clinte terminar a função, ele tera a escolha de voltar ao menu, sem ele precisar de exclui e abrir o terminal
   
    
    
    
    
    
    
    
menu()









 














