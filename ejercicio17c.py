frutas = ["manzana", "platano", "naranja"]
salir = True
print("""
1. Ver lista completa: Muestra la lista completa por pantalla.
2. Ver un elemento por índice: Pide una posición al usuario y muestra el elemento guardado en dicho índice.
3. Añadir elemento: Pide el nombre de una nueva fruta y la añade al final de la lista.
4. Modificar elemento: Pide la posición que se desea cambiar y el nuevo nombre para actualizar ese valor en la lista.
5. Borrar elemento: Pide el índice del elemento que se quiere eliminar y lo quita de la lista.
6. Salir: Muestra un mensaje de despedida y finaliza la ejecución del programa.
""")
while salir:
    opcion = int(input("Escribe la opcion: "))
    match opcion:
        case 1:
            print(frutas)
        case 2:
            posicion = int(input(f"Di la posicion que quieras ver (0 a {len(frutas) - 1}): "))
            if posicion < 0 or posicion >= len(frutas):
                print("La posicion es mayor que los elementos de la lista")
            else:
                print(frutas[posicion])
        case 3:
            nuevo = input("Escribe la fruta a añadir: ")
            frutas.append(nuevo)
        case 4:
            posicion = int(input(f"Di la posicion que deseas cambiar (0 a {len(frutas) - 1}): "))
            if posicion < 0 or posicion >= len(frutas):
                print("La posicion es mayor que los elementos de la lista")
            else: 
                fruta_nueva = input("Escribe la nueva fruta: ")
                frutas[posicion] = fruta_nueva
        case 5:
            borrar = int(input(f"Di la posicion que quieras borrar (0 a {len(frutas) - 1}): "))
            if borrar < 0 or borrar >= len(frutas):
                print("La posicion es mayor que los elementos de la lista")
            else: 
                fruta_borrada = frutas.pop(borrar)
                print(f"Se borró {fruta_borrada}")
        case 6:
            print("Adios")
            salir = False
        case _:
            print("Opcion no valida")