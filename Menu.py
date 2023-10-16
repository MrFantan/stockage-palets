import pandas as pd

# Cargar el archivo de datos
df = pd.read_excel("./Datos/basedatos/Almacen.xlsx")

# Definiciones para las opciones del menú
opcion_ingresar = "I"
opcion_buscar_cliente = "C"
opcion_buscar_referencia = "R"
opcion_eliminar = "E"
opcion_borrar_index = "B"
opcion_ver_todo = "V"
opcion_crear_qr = "Q"
opcion_salir = "S"


# Use el qrcreador módulo para crear códigos QR aquí
def crear_qr(text):
    pass

# Menú
while True:
    menu = input(
        "================================== \n"
        "ALMACEN \n"
        "================================== \n"
        "[I]ngresar datos \n"
        "[C]liente a buscar \n" 
        "[R]eférencia a buscar \n" 
        "[E]liminar reférencia \n"
        "[Q]R para crear \n"
        "[B]orrar Índice \n"
        "[V]er todo \n"
        "[S]alir \n"
        "================================== \n" 
        "Seleccione una opción: "
    ).upper()
    
    if menu == opcion_ingresar:
        from almacen import ingresar_datos # Importa la función desde el módulo "almacen"
        ingresar_datos()
        print("Datos insertados correctamente")
    elif menu == opcion_buscar_cliente:
        buscar = input("Que cliente busca: ")
        print(df[df['Cliente'] == buscar.upper()])
    elif menu == opcion_buscar_referencia.upper():
        buscar = input("Que Referencia busca: ")
        print(df[df['Referencia'] == buscar.upper()])
    elif menu == opcion_eliminar:
        eliminar = input("Ingrese la referencia a eliminar: ")
        referencia_a_eliminar = df[df['Referencia'].str.upper() == eliminar.upper()].index
        df = df.drop(referencia_a_eliminar)
        print(f"Se ha eliminado la reférencia {eliminar} de la base de datos.")
        df.to_excel("./Datos/almacen.xlsx", index=False)
    elif menu == opcion_borrar_index:
        borrar = input("Ingrese el ÍNDICE a eliminar: ")
        try:
            borrar = int(borrar)  # Convierte la entrada a un número entero si es posible
            index_a_eliminar = df[df['Índice'] == borrar].index
            if not index_a_eliminar.empty:
                df = df.drop(index_a_eliminar)
                print(f"Se ha eliminado el ÍNDICE {borrar} de la base de datos.")
                df.to_excel("./Datos/Basedatos/Almacen.xlsx", index=False)
            else:
                print(f"No se encontró ningún registro con el ÍNDICE {borrar}.")
        except ValueError:
            print("Ingrese un valor numérico para el ÍNDICE.")
    elif menu == opcion_crear_qr.upper():
        import qrcreador # Importa la función desde el módulo qrcreador.py
    elif menu == opcion_ver_todo:
        print(df)
    elif menu == opcion_salir:
        print("Gracias por su consulta, espero verle pronto.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")