class Empleado:
    def __init__(self, nombre, sueldo_base):
        if nombre is None:
            raise NameError("Falta el nombre")
        if sueldo_base < 0 or sueldo_base > 200000:
            raise ValueError("El sueldo tiene que ser mayor a 0 y menor a 200000")
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
    def getNombre(self):
        return self.__nombre
    def getSueldo_base(self):
        return self.__sueldo_base
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setSueldo_base(self, sueldo_base):
        self.__sueldo_base = sueldo_base
    def calcular_sueldo(self):
        return self.__sueldo_base

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        if comision > sueldo_base/2:
            raise ValueError("La comision tiene que ser menor del 50% del sueldo base")
        self.__comision = comision
    def getComision(self):
        return self.__comision
    def setComision(self, comision):
        self.__comision = comision
    def calcular_sueldo(self):
        return self.__sueldo_base+self.__comision

class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        if bono_gestion > sueldo_base/2:
            raise ValueError("El bono de gestion tiene que ser menor del 50% del sueldo base")
        self.__bono_gestion = bono_gestion
    def getBono_gestion(self):
        return self.__bono_gestion
    def setBono_gestion(self, bono_gestion):
        self.__bono_gestion = bono_gestion
    def calcular_sueldo(self):
        return self.__sueldo_base+self.__bono_gestion

empleado = Empleado("Ana", 1200)
vendedor = Vendedor("Carlos", 1200, 350)
gerente = Gerente("Marta", 2000, 500)
