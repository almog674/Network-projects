import socket


# Creating a socket object
my_socket = socket.socket()


my_socket.connect(('127.0.0.1', 8820))

user_data = input('waht do you want to sent to the server?')
my_socket.send(user_data.encode())
data = my_socket.recv(1024).decode()

print('data sent: ' + data)


my_socket.close()