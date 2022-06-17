import socket
import threading

nickname = input('Choose a nickname: ')


IP = '127.0.0.1'
PORT = 6666

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'NICK':
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print('Something went wrong...')
            client.close()
            break

def write():
    while True:
        message = nickname + ": " + input('')
        client.send(message.encode())

recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()