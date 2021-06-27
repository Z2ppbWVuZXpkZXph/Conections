import socket

GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"  # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"   # White
R = "\033[31m"    # Red
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

import socket
def obtener_info_equipo():
               nombre_equipo = socket.gethostname()
               direccion_equipo = socket.gethostbyname(nombre_equipo)
               print ("el nombre del equipo es: %s" % nombre_equipo)
               print ("La IP es: %s" % direccion_equipo)

# Crea socket IPv4 TCP, lo asocia al puerto 12345, y lo pone en escucha
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('192.168.1.43', 4002))
servidor.listen(5)
equipo = socket.gethostname()

print (GG +"        Servidor creado con exito!")

while True:
       cliente, direccion = servidor.accept()
       print (YY +'   [+] Se unio al chat:'+ WW, equipo)
       cliente.send(b'        Bienvenido a mi servidor')
       while True:
              mensaje_codificado = cliente.recv(5000)
              mensaje_decodificado = mensaje_codificado.decode('utf-8')
              print (RR +'Mensaje recibido:'+ WW, mensaje_decodificado)
              mensaje = input(BB +"Pon un mensaje: " + WW)
              if mensaje == "exit":
                     cliente.send(b"El servidor se cerrara, por favor, sal del chat")
                     servidor.close()
                     break
              else:
                     mensaje_codificado1 = bytes(mensaje, encoding = "utf-8")
                     cliente.send(mensaje_codificado1)
                     if mensaje_decodificado == b"":
                            break

