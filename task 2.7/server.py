#   Ex. 2.7 template - server side
#   Author: Barak Gonen, 2017
#   Modified for Python 3, 2020

import socket
import pyautogui as pag
import os
import shutil
import subprocess


IP = socket.gethostname()
PORT = 8820


def receive_client_request(client_socket):
    command_len = client_socket.recv(2).decode()
    command = client_socket.recv(int(command_len)).decode()
    print(command)
    return command


def check_client_request(command):
    valid = 1
    error_msg = None
    return valid, error_msg


def handle_client_request(command):
    replay_type = ''

    if command == 'screenshot':
        image = pag.screenshot()
        image.save(r'C:\screenshot\screen.jpg')
        replay = open(r'C:\screenshot\screen.jpg', encoding='latin-1')
        print(replay)
        replay_type = 'image'

    elif command == 'dir':
        path = os.listdir(r'C:\screenshot')
        files_list = os.listdir()
        print(files_list)
        replay = files_list
        replay_type = 'dir'

    elif command[0:6] == 'delete':
        file = command[::2]
        print('.\\' + command[7::])
        os.remove('.\\' + command[7::])
        replay = 'deleted succssesfuly!!'

    elif command[0:4] == 'copy':
        command = command.split(sep = ' ', maxsplit = 2)
        if len(command) == 3:
            choose_file = command[1]
            new_place = command[2]
            shutil.copy(choose_file, new_place)
            replay = 'Copied succssesfuly!!'
        else:
            replay = ('Somthing went wrong...')

    elif 'execute' in command:
        command = command.split(sep = ' ', maxsplit = 1)
        if len(command) != 2:
            replay = ('Somthing went wrong...')
        else:
            subprocess.call(command[1])
            replay = 'Execute Succssesfuly!!'

    else:
        print('not workind:(' + command[0:4])
        pass

    return replay, replay_type


def send_response_to_client(response, client_socket, response_type = 'reg'):
    if response_type == 'image':
        load_image = response.read(9999)
        while load_image:
            client_socket.send(load_image.encode())
            load_image = response.read(9999)
    if response_type == 'dir':
        client_socket.send(str(response).encode())
    else:
        client_socket.send(response.encode())


def main():
    # open socket with client
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP, PORT))
    server_socket.listen()
    print('The server is up and ready')
    client_socket, address = server_socket.accept()

    # handle requests until user asks to exit
    done = False
    while not done:
        command = receive_client_request(client_socket)
        valid, error_msg = check_client_request(command)
        if valid:
            response, response_type = handle_client_request(command)
            send_response_to_client(response, client_socket, response_type)
        else:
            send_response_to_client(error_msg, client_socket)

        if command == 'EXIT':
            done = True

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()