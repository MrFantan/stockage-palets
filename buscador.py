import pandas as pd

df = pd.read_excel("./Datos/almacen.xlsx")

respuesta = input("Menú Principal: \n 1.- Ingresar datos \n 2.- Buscar por cliente \n 3.- Buscar por reférencia \n 4.- Eliminar reférencia \n 0.- Salir \n Seleccione una opción: ")

ingresar = "1"
cliente = "2"
buscar = "3"
eliminar = "4"
salir = "0"


if respuesta == ingresar:
    from almacen import ingresar_datos
    print("Datos insertados correctamente")
elif respuesta == cliente:
    buscar = input("Que cliente busca: ")
    print(df[df['Cliente'] == buscar.upper()])
elif respuesta == buscar:
    buscar = input("Que reférencia busca: ")
    print(df[df['Referencia'] == buscar.upper()])
else:
    respuesta = salir
    print("Gracias por su consulta, espero verle pronto.")
