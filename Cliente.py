import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.connect(("127.0.0.3", 444))
mensaje = input("Manda un mensaje: ")
mensaje_listo = str.encode(mensaje, "utf-8")
servidor.send(mensaje_listo)
mensaje_recibido = servidor.recv(1024)
mensaje_decodificado = mensaje_recibido.decode("utf-8")
print ("Mensaje recibido:", mensaje_decodificado)
servidor.close()
