# 1 Importar librerias
import os
import pandas as pd

# 2 Definir variables
nombre_archivo = "Ej 27 Pandas 1 Datos.xlsx"
nombre_hoja = "Alumnos"
dic_datos = {}

# 3 Abrir el Excel con ExcelFile
excel = pd.ExcelFile(nombre_archivo)

# 4 Leer la hoja "Alumnos" en un DataFrame (df)
df = pd.read_excel(excel, sheet_name=nombre_hoja, index_col=None)
df = df.fillna("")
print(df)

# 5 Convertir el DataFrame a diccionario usando orient="records"
dic_datos[nombre_hoja] = df.to_dict(orient="records")
print(dic_datos)