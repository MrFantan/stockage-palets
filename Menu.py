import pandas as pd

# Cargar el archivo de datos
df = pd.read_excel("./Datos/almacen.xlsx")


# Definiciones para las opciones del menú

opcion_ingresar = "I"
opcion_buscar_cliente = "C"
opcion_buscar_referencia = "R"
opcion_eliminar = "E"
opcion_ver_todo = "V"
opcion_salir = "S"



menu = input(
        "================================== \n"
        "ALMACEN \n"
        "================================== \n"
        "[I]ngresar datos \n"
        "[C]liente a buscar \n" 
        "[R]eférencia a buscar \n" 
        "[E]liminar reférencia \n"
        "[V]er todo \n" 
        "[S]alir \n"
        "================================== \n" 
        "Seleccione una opción: "
        ).upper()


if menu == opcion_ingresar:
    from almacen import ingresar_datos
    print("Datos insertados correctamente")
elif menu == opcion_buscar_cliente.upper():
    buscar = input("Que cliente busca: ")
    print(df[df['Cliente'] == buscar.upper()])
elif menu == opcion_buscar_referencia.upper():
    buscar = input("Que Referencia busca: ")
    print(df[df['Referencia'] == buscar.upper()])
elif menu == opcion_eliminar:
    eliminar = input("Ingrese la referencia a eliminar: ")
    referencia_a_eliminar = df[df['Referencia'].str.upper() == eliminar.upper()].index
    df = df.drop(referencia_a_eliminar)
    print(print(f"Se ha eliminado la reférencia {eliminar} de la base de datos."))
    df.to_excel("./Datos/almacen.xlsx", index=False) 
elif menu == opcion_buscar_referencia.upper():
    buscar = input("Que reférencia busca: ")
    print(df[df['Referencia'] == buscar.upper()])    
elif menu == opcion_ver_todo:
    print(df)
else:
    respuesta = opcion_salir
    print("Gracias por su consulta, espero verle pronto.")