MARCAS_MODELOS = { "Seat": ["Ibiza", "Leon", "Ateca", "Arona"], "Toyota": ["Corolla", "Yaris", "RAV4", "C-HR"] }
ventas = [
["Seat", "Ibiza", 2024, 2023, 18000], ["Seat", "Ibiza", 2024, 2024, 18500], ["Seat", "Ibiza", 2024, 2024, 19000],
["Seat", "Ibiza", 2025, 2024, 19500], ["Seat", "Ibiza", 2025, 2025, 20000], ["Seat", "Ibiza", 2025, 2025, 20200],
["Seat", "Ibiza", 2026, 2025, 20500], ["Seat", "Ibiza", 2026, 2026, 21000], ["Seat", "Ibiza", 2026, 2026, 21500],
["Seat", "Leon", 2024, 2024, 24000], ["Seat", "Leon", 2024, 2024, 24500], ["Seat", "Leon", 2024, 2023, 23800],
["Seat", "Leon", 2025, 2025, 25500], ["Seat", "Leon", 2025, 2025, 26000], ["Seat", "Leon", 2025, 2024, 25200],
["Seat", "Leon", 2026, 2026, 27000], ["Seat", "Leon", 2026, 2026, 27500], ["Seat", "Leon", 2026, 2025, 26800],
["Seat", "Ateca", 2024, 2024, 28000], ["Seat", "Ateca", 2025, 2025, 29500], ["Seat", "Ateca", 2026, 2026, 31000],
["Seat", "Arona", 2024, 2024, 21000], ["Seat", "Arona", 2025, 2025, 22000], ["Seat", "Arona", 2026, 2026, 23000],
["Toyota", "Corolla", 2024, 2024, 26000], ["Toyota", "Corolla", 2024, 2024, 26500], ["Toyota", "Corolla", 2024, 2023, 25800],
["Toyota", "Corolla", 2025, 2025, 27500], ["Toyota", "Corolla", 2025, 2025, 28000], ["Toyota", "Corolla", 2025, 2024, 27200],
["Toyota", "Corolla", 2026, 2026, 29000], ["Toyota", "Corolla", 2026, 2026, 29500], ["Toyota", "Corolla", 2026, 2025, 28800],
["Toyota", "Yaris", 2024, 2024, 20000], ["Toyota", "Yaris", 2025, 2025, 21000], ["Toyota", "Yaris", 2026, 2026, 22000],
["Toyota", "RAV4", 2024, 2024, 38000], ["Toyota", "RAV4", 2025, 2025, 39500], ["Toyota", "RAV4", 2026, 2026, 41000],
["Toyota", "C-HR", 2024, 2024, 31000], ["Toyota", "C-HR", 2025, 2025, 32500], ["Toyota", "C-HR", 2026, 2026, 34000]
]


print("""
==========================================
SISTEMA DE GESTIÓN DE VENTAS
==========================================
1.- Dar de alta una nueva venta
2.- Resumen de ventas (Marca_Modelo_Año)
3.- Resumen de ventas (Marca_Modelo - Todos los años)
4.- Resumen de ventas (Marca - Todos los modelos y años)
5.- Salir del programa
""")


salir = True

while salir:
    opcion = int(input("Escribe la opción: "))

    match opcion:
        case 1:
            while True:
                print(MARCAS_MODELOS.keys())
                marca = str(input("Escribe el nombre de la marca: ")).capitalize()
                if MARCAS_MODELOS.__contains__(marca):
                    break
                else:
                    print("La marca no existe")

            while True:
                print(MARCAS_MODELOS[marca])
                modelo = str(input("Escribe el modelo: ")).capitalize()
                if MARCAS_MODELOS[marca].__contains__(modelo):
                    break
                else:
                    print("El modelo no existe")
            try:
                añoVenta = int(input("Escribe el año de venta, entre 2024 y 2026: "))
                if añoVenta < 2024 or añoVenta > 2026:
                    raise ValueError
                añoFabricacion = int(input(f"Escribe el año de fabricacion, entre 1990 y {añoVenta}: "))
                if añoFabricacion < 1990 or añoFabricacion > añoVenta:
                    raise ValueError
                precio = int(input("Escribe el precio, entre 1000€ y 100 000€: "))
                if precio < 1000 or precio > 100000:
                    raise ValueError
                
                ventas.append([marca, modelo, añoVenta, añoFabricacion, precio])
                print("Se ha completado la venta")
                print(ventas[-1])
            except ValueError:
                print("Error: Revisa bien los datos")
        case 2:
            resumenPunto2 = {}
            for venta in ventas:
                clave = f"{venta[0]}_{venta[1]}_{venta[2]}"
                if clave not in resumenPunto2:
                    resumenPunto2[clave] = [0,0]
                resumenPunto2[clave][0] += 1
                resumenPunto2[clave][1] += venta[4]
            print(resumenPunto2)
        case 3:
            resumenPunto3 = {}
            for venta in ventas:
                clave = f"{venta[0]}_{venta[1]}"
                if clave not in resumenPunto3:
                    resumenPunto3[clave] = [0,0]
                resumenPunto3[clave][0] += 1
                resumenPunto3[clave][1] += venta[4]
            print(resumenPunto3)
        case 4:
            resumenPunto4 = {}
            for venta in ventas:
                clave = f"{venta[0]}"
                if clave not in resumenPunto4:
                    resumenPunto4[clave] = [0,0]
                resumenPunto4[clave][0] += 1
                resumenPunto4[clave][1] += venta[4]
            print(resumenPunto4)
        case 5:
            salir = False
