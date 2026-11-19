# 1 Importar libreria
import pandas as pd

# 2 Definir variables
nombre_archivo = "Ej 27 Pandas 1.xlsx"
nombre_hoja = "Alumnos"
datos = {}

# 3 Abrir el Excel con ExcelFile
excel = pd.ExcelFile(nombre_archivo)

# 4 Leer la hoja "Alumnos" en un DataFrame (df)
df = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None)
df = df.fillna("")
print(df)

# 5 Convertir el DataFrame a diccionario usando orient="records"
datos[nombre_hoja] = df.to_dict(orient="records")
print(datos)

print("----")
# 6 Recorrer e imprimir dato a dato
for alumno in datos[nombre_hoja]:
    print(alumno)
    print(".-.-.")
    for clave, valor in alumno.items():
        print(f"{clave} - {valor}")
    print("----")

# PARTE 2
# orient="dict"
datos_dict = df.to_dict(orient="dict")
print(datos_dict)
for columna, filas in datos_dict.items():
    for indice, valor in filas.items():
        print(f"Columna: {columna}, Indice: {indice} - Valor: {valor}")
    print(".-.-.")
print("---------")
# orient="index"
datos_index = df.to_dict(orient="index")
print(datos_index)
for indice, alumno in datos_index.items():
    for columna, valor in alumno.items():
        print(f"Indice: {indice}, Columna: {columna} - Valor: {valor}")
    print(".-.-.")
print("---------")
# orient="list"
datos_list = df.to_dict(orient="list")
print(datos_list)
for columna, lista_valores in datos_list.items():
    for valor in lista_valores:
        print(f"Columna: {columna} - Valor: {valor}")
    print(".-.-.")
print("---------")

# Parte 3
df_indice = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=0)
print(df_indice)

# orient= "dict"
datos_dict_id = df_indice.to_dict(orient="dict")
print(datos_dict_id)
for columna, alumnos in datos_dict_id.items():
    for id_persona, valor in alumnos.items():
        print(f"Columna: {columna}, Id_Persona: {id_persona} - Valor: {valor}")
    print(".-.-.")
print("---------")

# orient="index"
datos_index_id = df_indice.to_dict(orient="index")
print(datos_index_id)
for id_persona, datos_alumno in datos_index_id.items():
    for columna, valor in datos_alumno.items():
        print(f"Id_Persona: {id_persona}, Columna: {columna} - Valor: {valor}")
    print(".-.-.")
print("---------")