import socket
import random

port_global = 8820
state_global = 'server'

class Socket:
    def choose_state(self, state, port):
        if state == 'client':
            self.__class__ = Client
            self.__init__('127.0.0.1', port)
        elif state == 'server':
            self.__class__ = Server
            self.__init__('0.0.0.0', port)

           
    def __init__(self, state, port):
        self.state = state
        self.port = port
        self.choose_state(self.state, self.port)








class Client(Socket):
    def initialize_client(self):
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.ip, self.port))
        print('Client Connected Succssesfuly')
        return socket_client


    def send_message(self, socket_client):
        data = input('What do you want to sent to the server: ')
        if 'exit' in data:
            self.end_connection(socket_client)
        else:
            socket_client.send(data.encode())


    def recv_message(self, socket_client):
        data = socket_client.recv(1024).decode()
        data = data.split(sep = '-')
        print('The server said: ' + data[0])
        new_port = int(data[1])
        return new_port


    def set_new_port(self, new_port):
        global port_global
        port_global = new_port

    def end_connection(self, socket_client):
        socket_client.close()


    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        socket_client = self.initialize_client()
        self.send_message(socket_client)
        new_port = self.recv_message(socket_client)
        self.set_new_port(new_port)
        self.end_connection(socket_client)
        server = Socket('server', port_global)


    







class Server(Socket):
    def initialize_server(self):
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind((self.ip, self.port))
        socket_server.listen()
        print('The server is up and ready')

        server_client, client_address = socket_server.accept()
        print('Client Connected Succssesfuly')

        return (socket_server, server_client)



    def recv_message(self, server_client):
        data = server_client.recv(1024).decode()
        if 'exit' in data:
            self.end_connection(socket_server, server_client)
        else:
            pass
        return data


    def get_random_port(self):
        new_port = random.randint(5000, 10000)
        return new_port


    def send_response(self, server_client, data, new_port):
        replay = 'Did you said ' + data + '?' + '-' + str(new_port)
        server_client.send(replay.encode())


    def set_new_port(self, port):
        global port_global
        port_global = port


    def end_connection(self, socket_server, server_client):
        server_client.close()
        socket_server.close()
        print('Client Disconnected')


    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        socket_server, server_client = self.initialize_server()
        data = self.recv_message(server_client)
        new_port = self.get_random_port()
        self.send_response(server_client, data, new_port)
        self.set_new_port(new_port)
        self.end_connection(socket_server, server_client)
        client = Socket('client', port_global)
        





client = Socket(state_global, port_global)
