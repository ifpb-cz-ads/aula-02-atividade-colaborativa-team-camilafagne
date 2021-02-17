dia = int(input("Informe o valor do dia: "))

hora = int(input("Informe o valor da hora: "))

minuto = int(input("Informe o valor do minuto: "))

segundo = int(input("Informe o valor do segundo: "))

dia = dia * 86400
hora = hora * 3600
minuto = minuto * 60
print("o total é: ", dia + hora + minuto + segundo)