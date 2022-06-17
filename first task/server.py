import socket

socket_server = socket.socket()
socket_server.bind(('0.0.0.0', 8820))

socket_server.listen()
print('The server is up and ready')

(clien_socket, client_address) = socket_server.accept()
print('Client connected!!')

data = clien_socket.recv(1024).decode()
print('Client Said: ' + data)

replay = "Hello " + data
clien_socket.send(replay.encode())

clien_socket.close()
socket_server.close()