import threading
import socket


IP = '127.0.0.1'
PORT = 9999
DISCONNECTION_MESSAGE = '*'


class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        self.client = self.initialize_client(self.IP, self.PORT)
        print('Client is up and ready!!')
        self.recieve_thread = threading.Thread(target = self.recieve)
        self.recieve_thread.start()

        self.write_thread = threading.Thread(target = self.write)
        self.write_thread.start()

    def initialize_client(self, IP, PORT):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP, PORT))
        return client


    def recieve(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                print(message)
            except:
                print('Something went wrong...')
                self.client.close()
                break

    def write(self):
        while True:
            message = input('')
            self.client.send(message.encode())
            if message == DISCONNECTION_MESSAGE:
                self.client.close()
                break




almog = Client(IP, PORT)