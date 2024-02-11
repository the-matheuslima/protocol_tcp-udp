import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#basic for socket udp
# try:
#     client.sendto(b"Cyber", ("127.0.0.1", 4433))
#     data, sender = client.recvfrom(1024)
#     print(sender[0] + ":" , data.decode())
#
# except Exception as error:
#     print("Error connection")
#     print(error)

#conversetion with socket
try:
    while True:
        msg = input("Mensagem: ") + "\n"
        client.sendto(msg.encode(), ("", 4433))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ":" , data.decode())
        if data.decode() == "sair\n" or msg == "sair\n":
            break
    client.close()

except Exception as error:
    print("Error connection")
    print(error)
