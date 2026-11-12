salir = True

while salir:
    opcion = int(input("Que ejercicio quieres ver (9-13) - 6 para salir "))

    match opcion:
        case 9:
            metros = float(input("Pon los metros que quieres pasar a centimetros: "))

            centimetros = metros*100
            print(f"{centimetros}cm")
        case 10:
            radio = float(input("Di el radio del circulo: "))

            area = 3.1415 * (radio**2)

            print(area)
        case 11:
            comida = float(input("Escribe cuanto costó la comida: "))
            propina = int(input("Di el porcentaje de propina que dejas: "))

            propina = propina/100

            total = (comida*propina) + comida

            print(total)
        case 12:
            peso = float(input("Escribe tu peso en kg: "))
            altura = float(input("Escribe tu altura en m: "))

            imc = peso / (altura**2)

            print(imc)
        case 13:
            nombre = input("Escribe tu nombre: ")
            apellido = input("Escribe tu apellido: ")

            print(f"Hola {nombre} {apellido}")
        case 6:
            salir = False
        case _:
            print("Solo del 9 al 13, para salir el 6")
        
