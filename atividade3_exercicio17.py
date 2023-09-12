def imposto():
    compra = float(input('Digite o valor da sua compra: '))
    imposto = float(input('Digite o valor do imposto a ser cobrado: '))
    imposto_soma = (imposto/100)*compra

    valor_total = compra+imposto_soma
    print('O valor total da sua compra com os adicionar de imposto ficou no valor de ' , valor_total , ' R$ REAIS')


imposto()