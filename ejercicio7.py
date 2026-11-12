numero1 = int(input("Pon el primer numero: "))
numero2 = int(input("Pon el segundo numero: "))

if numero2 == 0:
    print("No se puede dividir entre 0")
else:
    division = numero1 // numero2
    print(division)