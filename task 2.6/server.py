import socket
import time
import random

server = socket.socket()
server.bind(('0.0.0.0', 8820))

server.listen()
print('The server is up and ready')

(client_socket, client_address) = server.accept()
print('Client Coneected!!')


data_len = client_socket.recv(2).decode()
data = client_socket.recv(int(data_len)).decode()

N = 0
while data != 'quit' and N < 10:
    if data == 'Time':
        t = time.localtime()
        current_time = time.strftime('%H:%M:%S', t)
        client_socket.send(current_time.encode())
    elif data == 'Name':
        replay = 'Almog'
        client_socket.send(replay.encode())
    elif data == 'Rand':
        replay = random.randint(1,10)
        client_socket.send(str(replay).encode())
    elif data == 'What do you think about Hank':
        replay = "He's a great person and also the best charester in Breaking Bed"
        client_socket.send(str(replay).encode())
    else:
        replay = 'Unknown command'
        client_socket.send(replay.encode())

    data_len = client_socket.recv(2).decode()
    data = client_socket.recv(int(data_len)).decode()
    N = N + 1

client_socket.send('Connection Lost'.encode())
client_socket.close()
server.close()