import socket


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCCONECTING_MESSAGE = '*'

def initialize_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    return client

def send_message(message, client):
    message = message.encode()
    message_length = len(message)
    send_length = str(message_length).encode()
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def get_response(client):
    response = client.recv(1024).decode()
    print(response)
    return response

def main():
    client = initialize_client()
    send_message('hello world', client)
    response = get_response(client)
    send_message(DISCCONECTING_MESSAGE, client)
    
if __name__ == "__main__":
    main()