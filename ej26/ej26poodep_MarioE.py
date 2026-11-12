class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
    @property
    def nombre(self):
        return self.__nombre
    @property
    def sueldo_base(self):
        return self.__sueldo_base
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        self.__sueldo_base = sueldo_base
    def calcular_sueldo(self):
        return self.sueldo_base
    def __str__(self):
        return f"Empleado: {self.nombre}: {self.sueldo_base} €"
class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        self.comision = comision
    @property
    def comision(self):
        return self.__comision
    @comision.setter
    def comision(self, comision):
        self.__comision = comision
    def calcular_sueldo(self):
        return self.sueldo_base+self.comision
    def __str__(self):
        return f"Vendedor: {self.nombre}: {self.sueldo_base} € - {self.comision} €"

class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        self.bono_gestion = bono_gestion
    @property
    def bono_gestion(self):
        return self.__bono_gestion
    @bono_gestion.setter
    def bono_gestion(self, bono_gestion):
        self.__bono_gestion = bono_gestion
    def calcular_sueldo(self):
        return self.sueldo_base+self.bono_gestion
    def __str__(self):
        return f"Gerente: {self.nombre}: {self.sueldo_base} € - {self.bono_gestion} €"

class Departamento:
    def __init__(self, nombre, gerente: Gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @property
    def gerente(self):
        return self.__gerente
    @gerente.setter
    def gerente(self, gerente):
        self.__gerente = gerente
    def agregar_empleados(self, empleado):
        self.empleados.append(empleado)
    def nomina_total(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.calcular_sueldo()
        return total
    def __str__(self):
        resultado = f"Departamento: {self.nombre}\n{self.gerente}\n"
        for empleado in self.empleados:
            resultado += str(empleado) + "\n"
        resultado += f"Nomina total: {self.nomina_total()} €"
        return resultado
em1 = Empleado("Ana", 1200)
ve1 = Vendedor("Carlos", 1200, 350)
ge1 = Gerente("Marta", 2000, 500)

lista = [em1, ve1, ge1]

departamento1 = Departamento("Nacional", ge1 )
departamento2 = Departamento("Internacional", Gerente("John", 2500, 850))
departamento3 = Departamento("Nuevos Productos", Gerente("Marta", 2000, 450))

departamento1.agregar_empleados(em1)
departamento1.agregar_empleados(ve1)

departamento2.agregar_empleados(Vendedor("Sarah", 1500, 600))
departamento2.agregar_empleados(Vendedor("Pierre", 1500, 550))

departamento3.agregar_empleados(Empleado("Jaime", 1200))
departamento3.agregar_empleados(Vendedor("Secundino", 1200, 350))

print(departamento1)
print("-.-.-.-.-")
print(departamento2)
print("-.-.-.-.-")
print(departamento3)