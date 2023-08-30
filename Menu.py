import pandas as pd

df = pd.read_excel("./Datos/almacen.xlsx")

menu = input("Menú Principal: \n"
                  "1.- Ingresar datos \n" 
                  "2.- Buscar por cliente \n" 
                  "3.- Buscar por reférencia \n" 
                  "4.- Eliminar reférencia \n"
                  "5.- Ver todo \n" 
                  "0.- Salir \n"
                  "Seleccione una opción: "
                  )
ingresar = "1"
buscar_cliente = "2"
buscar_referecia = "3"
eliminar = "4"
todo = "5"
salir = "0"


if menu == ingresar:
    from Almacen import ingresar_datos
    print("Datos insertados correctamente")
elif menu == buscar_cliente:
    buscar = input("Que cliente busca: ")
    print(df[df['Cliente'] == buscar.upper()])
elif menu == buscar_referecia:
    buscar = input("Que Referencia busca: ")
    print(df[df['Referencia'] == buscar.upper()])
elif menu == eliminar:
    eliminar = input("Ingrese la referencia a eliminar: ")
    referencia_a_eliminar = df[df['Referencia'].str.upper() == eliminar.upper()].index
    df = df.drop(referencia_a_eliminar)
    print(print(f"Se ha eliminado la reférencia {eliminar} de la base de datos."))
    df.to_excel("./Datos/almacen.xlsx", index=False) 
elif menu == buscar_referecia:
    buscar = input("Que reférencia busca: ")
    print(df[df['Referencia'] == buscar.upper()])    
elif menu == todo:
    print(df)
else:
    respuesta = salir
    print("Gracias por su consulta, espero verle pronto.")