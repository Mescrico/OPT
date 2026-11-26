import pandas as pd
import pprint as pprint
from datetime import date
excel = pd.ExcelFile("PR01 Datos.xlsx")
nombres_hojas = excel.sheet_names


def cargar_datos():
    datos = {}
    for hoja in nombres_hojas:
        df = pd.read_excel(excel, sheet_name=hoja, index_col=None)
        df = df.fillna("")

        datos[hoja] = df.to_dict(orient="records")
        pprint.pprint(datos)
    return datos

def validar_email_corporativo(email_corporativo: str):
    return email_corporativo.strip().endswith('@g.educaand.es')

def alta_alumno(datos):
    id = str(input("Pon el id del alumno nuevo:")).strip().upper()
    nombre = str(input("Pon el nombre del alumno nuevo: ")).strip().title()
    email_corporativo = str(input("Pon el correo corporativo (@g.educaand.es): ")).strip()
    email_personal = f"{nombre}@gmail.com"
    grupo = str(input("Pon el grupo (DAW1 / DAW2): ")).strip().upper()
    fecha_ingreso = str(date.today())
