import pandas as pd

df = pd.read_excel("./Datos/almacen.xlsx")

respuesta = input("quieres buscar o ingresar? (B/I):  ")

buscar = "b"
ingresar = "i"

if respuesta != ingresar:
    print(df)
else:
    respuesta != buscar
    from almacen import ingresar_datos
