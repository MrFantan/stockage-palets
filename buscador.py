import pandas as pd

df = pd.read_excel("./Datos/almacen.xlsx")

respuesta = input("quieres buscar referencia, cliente o ingresar? (B/C/I):  ")

buscar = "b"
ingresar = "i"
cliente = "c"

if respuesta == ingresar:
    from almacen import ingresar_datos
    print("Datos insertados correctamente")
if respuesta == cliente:
    buscar = input("Que cliente busca: ")
    print(df[df['Cliente'] == buscar])
else:
    buscar = input("Que referencia busca: ")
    print(df[df['Referencia'] == buscar])

