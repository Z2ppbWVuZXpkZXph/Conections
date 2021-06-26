import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('127.0.0.3', 4000))
servidor.listen(5)

while True:
       cliente, direccion = servidor.accept()
       print('Acepta conexión del cliente', direccion)
       mensaje_codificado = cliente.recv(1024)
       mensaje_decodificado = mensaje_codificado.decode('utf-8')
       print('Mensaje recibido:', mensaje_decodificado)
       cliente.send(b'Gracias por conectarte')
       cliente.close()
