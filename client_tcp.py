import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('', 4422))
    client.send(b"Heloo!\n")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except Exception as error:
    print(error)
    print("Um erro ocorreu.")