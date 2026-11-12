productos = ["manzanas", "plátanos", "naranjas", "kiwis", "fresas"]
info_tienda = ("Frutería La Huerta", "Calle Mayor 12", "912345678", 2010)
precios = {"manzanas": 1.50, "plátanos": 2.10, "naranjas": 1.20,"kiwis": 3.45, "fresas": 2.80}

salir = True
print("""
1. Gestion de lista (productos)
2. Consulta de tupla (informacion de la tienda)
3. Gestion de Diccionario (precios por kilo)
4. Salir
""")
while salir:
    opcion = int(input("Escribe la opcion: "))
    match opcion:
        case 1:
            print("""
            a) Consultar
            b) Añadir
            c) Modificar
            d) Eliminar
            """)
            opcion = int(input("Escribe la opcion: "))
            match opcion:
                case 1:
                    for producto in productos:
                        print(f"Producto: {producto}")
                    print(f"Cantidad total: {len(productos)}")
                case 2:
                    nuevo = str(input("Escribe el nuevo producto: ").strip().lower())
                    productos.append(nuevo)
                    print(productos)
                case 3:
                    for i, producto in enumerate(productos):
                        print(f"Indice: {i}, producto: {producto}")
                    try:
                        modificar = int(input("Escribe el indice a modificar: "))
                        nuevo = str(input("Escribe el nuevo nombre: ").strip().lower())

                        if(modificar < 0 or modificar >= len(productos)):
                            raise IndexError
                        productos[modificar] = nuevo
                        print(productos)
                    except ValueError:
                        print("Error: Solo numeros enteros")
                    except IndexError:
                        print("Error: Solo indices que existan")
                case 4:
                    for i, producto in enumerate(productos):
                        print(f"Indice: {i}, producto: {producto}")

                    try:
                        eliminar = int(input("Escribe el indice a eliminar:"))

                        if(eliminar < 0 or eliminar >= len(productos)):
                            raise IndexError
                        productos.pop(eliminar)
                        print(productos)
                    except ValueError:
                        print("Error: Solo numeros enteros")
                    except IndexError:
                        print("Error: Solo indices que existan")
                case _:
                    print("Opcion no valida")
        case 2:
            print(info_tienda)
            print(f"Longitud mediante: {len(info_tienda)}")
            print("Elementos:")
            print(info_tienda[0])
            print(info_tienda[1])
            print(info_tienda[2])
            print(info_tienda[3])
        case 3:
            print("""
            a) Consultar catalogo completo
            b) Ver solo nombres / solo precios
            c) Añadir o actualizar
            d) Eliminar
            """)
            opcion = int(input("Escribe la opcion: "))
            match opcion:
                case 1:
                    print(precios.items())
                case 2:
                    print("""
                    a) Ver solo nombres
                    b) Ver solo precios
                    """)
                    opcion = int(input("Escribe la opcion: "))
                    match opcion:
                        case 1:
                            print(precios.keys())
                        case 2:
                            print(precios.values())
                        case _:
                            print("Opcion no valida")
                case 3:
                    nombre = str(input("Escribe el nombre de la fruta: ").strip().lower())

                    try:
                        precio = float(input("Escribe el precio: "))

                        if precio < 0:
                            raise ValueError

                        precios[nombre] = precio
                        print(f"Guardada la fruta {nombre} con precio {precio}€")

                    except ValueError:
                        print("Error: El precio no puede estar por debajo de 0")
                case 4:
                    nombre = str(input("Escribe el nombre de la fruta: ").strip().lower())

                    if nombre in precios:
                        precios.pop(nombre)
                        print(f"La fruta {nombre} se ha eliminado")
                    else:
                        print("No existe ninguna fruta con ese nombre")
                case _:
                    print("Escribe una opcion valida")
        case 4:
            print("Adios")
            salir = False