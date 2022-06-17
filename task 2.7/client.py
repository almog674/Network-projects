import socket
import glob

IP = socket.gethostname()
PORT = 8820


def valid_request(request):
    valid = 1
    return valid

def send_request_to_server(my_socket, request):
    request_len = str(len(request))
    zfill_len = request_len.zfill(2)
    request = zfill_len + request
    my_socket.send(request.encode())



    if request[2::] == 'screenshot':
        respons_type = 'image'
    elif request[2::] == 'dir':
        respons_type = 'dir'
    else:
        respons_type = 'reg'

    return respons_type



def handle_server_response(my_socket, request, request_type):
    
    if request_type == 'image':
        f = open('screenshot2.png', 'wb')
        load_image = my_socket.recv(9999)
        while load_image[0] != 0:
            f.write(load_image)
            load_image = my_socket.recv(9999)
        print(f)
    elif request_type == 'dir':
        data = my_socket.recv(1024).decode()
        print(data)
    else:
        data = my_socket.recv(1024).decode()
        print(data)


def main():
    # open socket with the server
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))

    # print instructions
    print('Welcome to remote computer application. Available commands are:\n')
    print('TAKE_SCREENSHOT\nSEND_FILE\nDIR\nDELETE\nCOPY\nEXECUTE\nEXIT')

    done = False
    # loop until user requested to exit
    while not done:
        request = input("Please enter command:\n")
        if valid_request(request):
            request_type = send_request_to_server(my_socket, request)
            handle_server_response(my_socket, request, request_type)
            if request == 'EXIT':
                done = True
    my_socket.close()

if __name__ == '__main__':
    main()