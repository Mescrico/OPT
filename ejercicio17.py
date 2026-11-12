ventas = [
    ("manzanas", 3, 2.7),
    ("peras", 2, 1.55),
    ("kiwi", 4, 2.9),
    ("granadina", 3, 2.5),
    ("platano", 1, 0.77)
]

totalGastado = 0

for producto, cantidad, precio in ventas:
    nombre = producto.upper()
    total = round(cantidad*precio, 2)
    totalGastado += total
    print(f"Producto: {nombre}, total: {total}€, total general: {round(totalGastado, 2)}€")
