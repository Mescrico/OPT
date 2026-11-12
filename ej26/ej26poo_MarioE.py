class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
    def calcular_sueldo(self):
        return self.sueldo_base

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision
    def calcular_sueldo(self):
        return self.sueldo_base+self.comision

class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion
    def calcular_sueldo(self):
        return self.sueldo_base+self.bono_gestion

lista = [Empleado("Ana", 1200), Vendedor("Carlos", 1200, 350), Gerente("Marta", 2000, 500)]

for trabajador in lista:
    print(f"Trabajador: {trabajador.nombre} - Cargo: {type(trabajador).__name__} - Sueldo: {trabajador.calcular_sueldo()}€")