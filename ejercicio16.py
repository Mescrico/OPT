salir = True

while salir:
    try:
        opcion = int(input("Que ejercicio quieres ver (9-13) - 6 para salir "))

        match opcion:
            case 9:
                metros = float(input("Pon los metros que quieres pasar a centimetros: "))

                if metros < 0:
                    raise ValueError("Los metros no pueden estar en negativo")
                centimetros = metros*100
                print(f"{centimetros}cm")
            case 10:
                radio = float(input("Di el radio del circulo: "))

                if radio < 0:
                    raise ValueError("El radio no puede ser negativo")
                area = 3.1415 * (radio**2)

                print(area)
            case 11:
                comida = float(input("Escribe cuanto costó la comida: "))
                propina = int(input("Di el porcentaje de propina que dejas: "))

                if comida < 0:
                    raise ValueError("La comida no puede ser negativa")
                elif propina < 0:
                    raise ValueError("La propina no puede ser negativa")

                propina = propina/100

                total = (comida*propina) + comida

                print(total)
            case 12:
                peso = float(input("Escribe tu peso en kg: "))
                altura = float(input("Escribe tu altura en m: "))

                if peso < 0:
                    raise ValueError("El peso no puede ser negativa")
                elif altura < 0:
                    raise ValueError("La altura no puede ser negativa")

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
    except ValueError as e:
        print(f"Error de valor: {e}")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
