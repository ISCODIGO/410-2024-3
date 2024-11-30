"""
Este proyecto permite descargar una imagen y escribirla en el directorio actual
"""

import socket

SERVIDOR = "data.pr4e.org"
PUERTO = 80
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misock.connect((SERVIDOR, PUERTO))
misock.sendall(b"GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n")
contador = 0
imagen = b""

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    # time.sleep(0.25)
    contador = contador + len(datos)
    print(len(datos), contador)
    imagen = imagen + datos

misock.close()

# Busqueda del final de la cabecera (2 CRLF)
pos = imagen.find(b"\r\n\r\n")
print("Header length", pos)
print(imagen[:pos].decode())

# Ignorar la cabecera y guardar los datos de la imagen
imagen = imagen[pos + 4:]
fhand = open("cosa.jpg", "wb")
fhand.write(imagen)
fhand.close()
