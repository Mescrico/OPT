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
datos = cargar_datos()
pprint(datos)
def guardar_datos():
    print("por hacer")

def validar_email_corporativo(email_corporativo: str):
    return email_corporativo.strip().endswith('@g.educaand.es')

def alta_alumno(datos):
    ids_alumnos = []
    for alumno in datos["Alumnos"]:
        ids_alumnos.append(alumno.get("id_persona", "").strip().upper())
        
    id = str(input("Pon el id del alumno nuevo:")).strip().upper()
    if id in ids_alumnos:
        print("Ese ID ya existe pon otro")
        return
    nombre = str(input("Pon el nombre del alumno nuevo: ")).strip().title()
    apellidos = str(input("Pon los apellidos del alumno nuevo: ")).strip().title()
    telefono = int(input("Pon el numero de telefono del alumno nuevo: "))
    email_corporativo = str(input("Pon el correo corporativo (@g.educaand.es): ")).strip()
    email_personal = str(input("Pon el correo personal: ")).strip().lower()
    grupo_actual = str(input("Pon el grupo (DAW1 / DAW2): ")).strip().upper()
    fecha_ingreso = str(date.today())
    curso_academico = '2026-2027'

    nuevo_alumno = {
        "id_persona": id,
        "nombre": nombre,
        "apellidos": apellidos,
        "telefono": telefono,
        "email_corporativo": email_corporativo,
        "email_personal": email_personal,
        "fecha_ingreso": fecha_ingreso,
        "fecha_salida": "",
        "grupo_actual": grupo_actual,
        "curso_academico": curso_academico
    }
    datos["Alumnos"].append(nuevo_alumno)

def alerta_personal_consejeria(datos):
    if datos["Conserjeria"] > 4:
        return "Sobra personal de consejeria"
    if datos["Conserjeria"] < 4:
        return "Falta personal de consejeria"
def alerta_turno_consejeria(datos):
    mañana = 0
    tarde = 0
    for conserjes in datos["Conserjeria"]:
        if conserjes.get("turno").strip().lower() == "mañana":
            mañana += 1
        if conserjes.get("turno").strip().lower() == "tarde":
            tarde += 1
    if mañana != 2 or tarde != 2:
        return "El personal de consejeria tiene que ser 2 de mañana y 2 de tarde"
