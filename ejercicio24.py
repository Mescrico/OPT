# 1. Lista
verduras = ["sandia","Lechuga", "Espinaca", "Coliflor", "Cebollino", "Ajo"]
verduras.append("Patata")
for verdura in verduras:
    print(verdura.upper())
    print(verdura.capitalize())
    print(verdura.lower())
    print("------")
# 2. Tupla
componentes = ("monitor", "raton", "teclado", "alfombrilla", "usb")
for componente in componentes:
    print(componente)
    print("------")

# 3. Diccionario con .items() obteniendo clave y valor juntos
biblioteca = {"Mario":"El quijote", "Oscar":"La bella y la bestia", "Secundino":"La biblia"}
print("CLAVE - VALOR")
for nombre, libro in biblioteca.items():
    print(f"{nombre} alquiló {libro}")
    print("------")

print("VALORES")
print("------")
for libro in biblioteca.values():
    print(libro)
print("------")

print("CLAVES")
print("------")
for nombre in biblioteca.keys():
    print(nombre)

print("------")
print("VALORES SIN .values()")
print("------")
for valor in biblioteca:
    print(biblioteca[valor])

# 6. Cadena de caracteres
print("------")
texto = "Javascript"
for letra in texto:
    print(letra*2, end=" ")