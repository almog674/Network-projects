from scapy.all import *
import socket


def get_user_input():
    message = input('What do you want to send? ')
    parts = input('How many parts? ')
    return (message, parts)

def build_packet(message, parts):
    packet = IP(src = '0.0.0.0', dst = '127.0.0.1')/UDP(dport = 55555, sport = 44444)/Raw(message + '/' + parts)
    return packet


def initialize_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return client
    
def send_packet(packet, client):
    packet_bytes = bytes(packet)
    dst_ip = packet[IP].dst
    dst_port = packet[UDP].dport
    client.sendto(packet_bytes, (dst_ip, dst_port))

def recieve_response(client, parts):
    full_response = ''
    for el in range(int(parts)):
        (response, server_address) = client.recvfrom(1024)
        response = response.decode()
        full_response = full_response + response
    return full_response

def print_response(response):
    print(response)


def main():
    message, parts = get_user_input()
    packet = build_packet(message, parts)
    client = initialize_client()
    send_packet(packet, client)
    response = recieve_response(client, parts)
    print_response(response)

    
if __name__ == '__main__':
    main()