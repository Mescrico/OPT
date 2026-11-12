comida = float(input("Escribe cuanto costó la comida: "))
propina = int(input("Di el porcentaje de propina que dejas: "))

propina = propina/100

total = (comida*propina) + comida

print(total)