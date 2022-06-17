from scapy.all import *
import socket
import math

def server_initialize():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('0.0.0.0', 55555))
    print('The server is up and ready!!')
    return server


def handle_client(server):
    (client_packet, client_address) = server.recvfrom(1024)
    clear_packet = scapy.layers.inet.IP(client_packet)
    print('packet recieved')
    return clear_packet, client_address

def seperete_data(clear_packet):
    data = clear_packet[Raw].load
    data = data.decode()

    splited_data = data.split(sep = '/', maxsplit = 1)
    message = splited_data[0]
    num_of_pragments = splited_data[1]

    return (message, num_of_pragments)

def check_validation(message, num_of_pragments):
    if num_of_pragments.isdigit() == False:
        valid = 'no'
        error_message = 'Only numbers allowd'
    elif int(num_of_pragments) > len(message):
        valid = 'no'
        error_message = 'Too many parts'
    else:
        valid = 'yes'
        error_message = ''

    return valid, error_message

def pragmentation(message, num_of_pragments):
    num_of_pragments = int(num_of_pragments)

    data_chunks = math.floor(len(message) / num_of_pragments)
    pragment_list = []
    for el in range(num_of_pragments):
        pragment = message[(data_chunks * el) : (data_chunks * (el + 1))]
        pragment_list.append(pragment)
    last_element = pragment + (message[(data_chunks * num_of_pragments) : len(message)])
    pragment_list[len(pragment_list) -1] = last_element
    return pragment_list

def send_pragments(pragments, client_address, server):
    for el in pragments:
        server.sendto(el.encode(), client_address)


def main():
    server = server_initialize()
    client_packet, client_address = handle_client(server)
    message, num_of_pragments = seperete_data(client_packet)
    valid, error_message = check_validation(message, num_of_pragments)
    if valid == 'yes':
        pragments = pragmentation(message, num_of_pragments)
        send_pragments(pragments, client_address, server)
    else:
        print(error_message)


if __name__ == '__main__':
    main()