preco = float(input("Informe o valor do preco: "))

percentual = float(input("Informe o percentual de desconto: "))

desconto = preco * percentual / 100
pagamento = preco - desconto
print("o desconto será de %.2f e deverá pagar %.2f" % (desconto,pagamento))