import pandas as pd

df = pd.read_excel("./Datos/almacen.xlsx")

respuesta = input("quieres buscar o ingresar? (B/I):  ")

buscar = "b"
ingresar = "i"

if respuesta == ingresar:
    from almacen import ingresar_datos
    print("Datos insertados correctamente")
else:
    buscar = input("Que referencia busca: ")
    print(df[df['Referencia'] == buscar])

