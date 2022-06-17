import socket
import select

PORT = 55555
SERVER_IP = '0.0.0.0'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen()
print('Server is up and ready!!')
open_client_sockets = []
messeges_to_send = []

while True:
    rlist, wlist, elist = select.select([server] + open_client_sockets, open_client_sockets, [])

    for client in rlist:
        if client is server:
            connection, client_address = server.accept()
            print('New Client Has Connected with the address: ', client_address)
            open_client_sockets.append(connection)
        else:
            data = client.recv(1024).decode()
            if data == '':
                print('Connection Closed...')
                open_client_sockets.remove(client)
                client.close()
            else:
                messeges_to_send.append((client, data))
    for messege in messeges_to_send:
        client, data = messege
        if client in wlist:
            data = 'Hello ' + data
            client.send(data.encode())

            print('Sended: ' + data + ' successfuly!!')
            messeges_to_send.remove(messege)

def print_clients(open_client_sockets):
    for c in open_client_sockets:
        print("\t", c.getpeername())