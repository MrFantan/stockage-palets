import pandas as pd
import qrcode
from PIL import Image
import os

# Directorio donde se guardarán los códigos QR
directorio = "Datos/QR"

# Crear el directorio si no existe
if not os.path.exists(directorio):
    os.makedirs(directorio)

# Leer el archivo XLSX
df = pd.read_excel("Datos/Basedatos/Almacen.xlsx")

# Solicitar al usuario que ingrese la referencia
referencia = input("Ingresa una referencia para realizar el codigo QR: ")

try:
    # Intentar convertir la referencia en un número de fila
    fila = int(referencia)
except ValueError:
    # Si no es un número, intentar encontrar la referencia en la base de datos
    try:
        fila = df.index[df["Referencia"] == referencia][0]
    except IndexError:
        # Si la referencia no se encuentra en la base de datos, informar al usuario y salir
        print(f"La referencia '{referencia}' no se encuentra en la base de datos.")
        exit()

# Obtener el texto de las celdas en la fila especificada
ref = df.at[fila, "Referencia"]
cli = df.at[fila, "Cliente"]
cal = df.at[fila, "Calle"]
bas = df.at[fila, "Base"]
alt = df.at[fila, "Altura"]
tra = df.at[fila, "Trabajador"]
fec = df.at[fila, "Fecha"]
hor = df.at[fila, "Hora"]

# Crear el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Concatenar todos los datos en una sola cadena
data = f"Referencia: {ref}\nCliente: {cli}\nCalle: {cal}\nBase: {bas}\nAltura: {alt}\nTrabajador: {tra}\nFecha: {fec}\nHora: {hor}"

qr.add_data(data)
qr.make(fit=True)

# Crear la imagen del código QR
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen
img.save(f'{directorio}/codigo_qr_{referencia}.png')

print(f"Código QR para la referencia '{ref}', cliente '{cli}' en la calle '{cal}' en base {bas} a la altura {alt} por trabajador '{tra}'el dia '{fec}', a la hora '{hor}' se ha generado con éxito.")
