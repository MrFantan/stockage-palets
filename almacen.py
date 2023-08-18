import openpyxl
from openpyxl import Workbook
import pandas as pd
from datetime import datetime

def ingresar_datos():
    referencia = input("Código de referencia: F")
    cliente = input("Nombre cliente: ")
    unidades = input("Unidades por embalaje: ")
    embalajes = input("Cantidad de cajas en el palet: ")
    cantidad_total = input("Cantidad total por palet: ")
    palets = input("Cantidad de palets: ")
    calle = input("En que calle esta ubicado A-F: ")
    base = input("En que base esta ubicado 1-33: ")
    altura = input("En que altura esta ubicado 0-8: ")
    trabajador = input("Cúal es su nombre: ")
    dia = datetime.today().strftime("%d/%m/%y")
    hora = datetime.today().strftime("%H:%M")


    datos = {
        "Referencia": "F"+referencia,
        "Cliente": cliente.upper(),
        "Unidades": unidades, 
        "Embalajes": embalajes,
        "Cantidad Total": cantidad_total,
        "Palets": palets,
        "Calle": calle.upper(),
        "Base": base,
        "Altura": altura,
        "Trabajador": trabajador. title(),
        "Fecha": dia,
        "Hora": hora,
    }

    try:
        workbook = openpyxl.load_workbook('./Datos/almacen.xlsx')
        sheet = workbook.active
    except FileNotFoundError:
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(["Referencia", "Cliente", "Unidades", "Embalajes", "Cantidad Total", "Palets", "Calle", "Base", "Altura", "Trabajador", "Fecha", "Hora"])

    values = list(datos.values())
    sheet.append(values)

    workbook.save('./Datos/almacen.xlsx')
    print(f"Se ha agregado al cliente {cliente} con la referencia número: F{referencia}, un total de {unidades} unidades por embalaje, distribuidas en {embalajes} cajas, con un total de {cantidad_total} unidades. Todo ha sido colocado en {palets} palets. Ubicado en Calle {calle} en la sección con base {base} y altura {altura} por el trabajador: {trabajador}, el día {dia} a las {hora}.")
    print("Producto almacenado exitosamente.")

while True:
    ingresar_datos()
    continuar = input("Desea Ingresar otra referencia? (s/n)")
    if continuar.lower() != "s":
        break

print("Programa finalizado.")
