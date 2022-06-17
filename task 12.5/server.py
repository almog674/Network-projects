import socket
import threading


IP = '0.0.0.0'
PORT = 9999
DISCONNECTION_MESSAGE = '*'

class Server:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        server = self.initialize_server(self.IP, self.PORT)
        self.clients = []
        clients = self.handle_connections(server, self.clients)
        while True:
            clients = self.handle_connections(server, clients)

    def initialize_server(self, IP, PORT):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((IP, PORT))
        server.listen()
        print('[SERVER] ready to start!!')
        return server

    def disconnection(self, server, client, clients):
        self.broadcast_message(server, client, f"[SERVER]: {client} has left the chat!", clients)
        # print(f"the client is: {client}")
        if client in clients:
            clients.remove(client)
        else:
            pass
        client.close()
        


    def handle_connections(self, server, clients):
        client, client_address = server.accept()
        print(f"[SERVER] {client_address} connected successfuly!")
        print(client)
        clients.append(client)
        self.broadcast_message(server, client, f"[SERVER] {client_address} has joined the chat!", clients)
        thread = threading.Thread(target = self.handle_client_request, args = (server, client, clients))
        thread.start()
        print(f'[SYSTEM]: there is {threading.activeCount() - 1} active connections')
        return clients

    def broadcast_message(self, server, client_sended, message, clients):
        clients_to_send = []
        for client in clients:
            clients_to_send.append(client)
        if client_sended in clients_to_send:
            clients_to_send.remove(client_sended)
        if len(clients_to_send) > 0:
            for client in clients_to_send:
                client.send(message.encode())
        else:
            pass

    def handle_client_request(self, server, client, clients):
        while True:
            try:
                message = client.recv(1024).decode()
                print(message)
                if message == DISCONNECTION_MESSAGE:
                    self.disconnection(server, client, clients)
                    break
                else:
                    self.broadcast_message(server, client, message, clients)
            except:
                self.disconnection(server, client, clients)
                break

almog = Server(IP, PORT)