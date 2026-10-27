x = []
valorBruto = 0

while True:
    compra = float(input("Digite o valor da compra (ou 0 para encerrar): "))
    if compra < 0:
        print("Por favor, digite um valor valido!")
        continue
    elif compra == 0:
        print("Programa encerrado.")
        break
    else:
        valorBruto = valorBruto + compra

    idade = int(input("Digite a idade: "))
    if idade < 0:
        idade = int(input("Digite uma idade valida: "))
    elif idade >= 130:
        idade = int(input("Digite uma idade valida: "))

    if compra > 100 and idade >= 65:
        compra = compra - (compra * 0.20) 
        if compra > 100:
            compra = compra - (compra * 0.10)
        print("O valor da compra é: R${:.2f}".format(compra))
        x.append(compra)
    
    elif idade >= 65 and compra <= 100:
        compra = compra - (compra * 0.20)
        print("O valor da compra é: R${:.2f}".format(compra))
        x.append(compra)
    
    elif compra >= 100:
        compra = compra - (compra * 0.10)
        print("O valor da compra é: R${:.2f}".format(compra))
        x.append(compra)
    
    else:
        print("O valor da compra é: R${:.2f}".format(compra))
        x.append(compra)

print("================= RESUMO DO DIA =================")
print("Total de compras: {}".format(len(x)))
print("O valor bruto é: R${:.2f}".format(valorBruto))
print("O valor total com desconto é: R${:.2f}".format(sum(x)))
print("O total de descontos concedidos é: R${:.2f}".format(valorBruto - sum(x)))
print("=================================================")
