import socket

client = socket.socket()
client.connect(('127.0.0.1', 8820))


def command_write():
    command = input('Write a command: ')
    length = str(len(command))
    zfill_length = length.zfill(2)
    command = zfill_length + command
    return command


show_menu = input('Do you want to see the menu? ')
if show_menu == 'yes':
        print('Menu: \nTime: ask the server for the current date \nName: get the server name \nRand: get a random number between 1-10')
else:
    pass


command = command_write()
while command != '04quit':
    client.send(command.encode())
    respons = client.recv(1024).decode()
    print(respons)
    command = command_write()
        


client.close()