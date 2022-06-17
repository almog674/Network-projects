import socket
import select


PORT = 55555
IP = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))
print('Ready to start!\n*************** \n\n')

while True:
    name = input('What is your name? ')
    client.send(name.encode())
    message = client.recv(1024).decode()
    print(message)

    if len(name) == 0:
        print('Closing connection')
        client.close()
