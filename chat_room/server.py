import socket
import threading

IP = '0.0.0.0'
PORT = 6666

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen()
print('Server is up and ready')

clients = []
nicknames = []

def broadcast_message(message):
    for client in clients:
        client.send(message.encode())

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast_message(message)
        except:
            index = clients.index(client)
            clients.remove(index)
            client.close()
            nickname = nicknames[index]
            broadcast_message(f'{nickname} has left the chat')
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client, client_address = server.accept()
        print(f"Connected with: {str(client_address)}")
        client.send('NICK'.encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(client)
        print(f"The nickname of this client is {nickname}")
        message = f"[SERVER] {nickname} is connected"
        broadcast_message(message)


        theade = threading.Thread(target = handle_client, args = (client,))
        theade.start()


recieve()