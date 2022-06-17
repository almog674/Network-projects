import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCCONECTING_MESSAGE = '*'

def initialize_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    print(server)
    return server

def handle_client(connection, address):
    connected = True
    while connected:
        message_length = connection.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            message = connection.recv(message_length).decode(FORMAT)
            print(f"[{address}] {message}")
            if message == DISCCONECTING_MESSAGE:
                connected = False
            response = '[SERVER] Message recieved: ' + str(message)
            connection.send(response.encode())
    connection.close()


def start(server):
    server.listen()
    while True:
        (client, client_address) = server.accept()
        theade = threading.Thread(target = handle_client, args = (client, client_address))
        theade.start()
        print(f"[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}")

def main():
    server = initialize_server()
    print('[SERVER] up and ready to start!!')
    start(server)


if __name__ == "__main__":
    main()