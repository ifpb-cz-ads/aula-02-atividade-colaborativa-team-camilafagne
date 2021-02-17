salario = float(input("Informe o salário: "))

aumento = float(input("Informe o aumento que deseja: "))

resultado= salario + (salario * aumento / 100)

print("O aumento do salário foi de %.2f" % resultado)