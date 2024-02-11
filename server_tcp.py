import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
file = open('output.txt', 'a')

try:
    server.bind(("0.0.0.0", 4422))
    server.listen(5)
    print("Listening...")

    client_socket, address = server.accept()
    print("Received from:" + address[0])


    data = client_socket.recv(1024).decode()
    print(data)
    client_socket.send(input("Mensagem: ").encode())

    file.write(data)

    server.close()

except Exception as error:
    print(error)
    server.close()
