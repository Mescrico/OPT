# Para el get es 
@property
def x(self):
    """Getter para x: devuelve el valor redondeado a un decimal"""
    return round(self._x, 1)

#Para el set es
@x.setter
def x(self, nuevo_x):
    """Setter para X: valida rango al hacer p.y = valor"""
    if nuevo_x < -100 or nuevo_x > 100:
        print("El nuevo x no puede estar entre -100 y 100")
    else:
        self._x = float(nuevo_x)