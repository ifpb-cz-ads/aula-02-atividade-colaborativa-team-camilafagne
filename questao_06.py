materia1= float(input('Informe a nota: '))
materia2= float(input('Informe a nota: '))
materia3= float(input('Informe a nota: '))

media = (materia1 + materia2 + materia3) / 3

if media > 7:
    print("Aprovado")
else:
    print("Reprovado")