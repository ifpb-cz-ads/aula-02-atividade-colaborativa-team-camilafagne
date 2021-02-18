kilometros = float(input("Informe a quantidade de kilometros percorrida: "))

dias = float(input("Informe a quantidade de dias: "))

pagamento = (kilometros * 0.15) + (dias * 60)

print ("Voce deverar pagar %2.f reais" % (pagamento))