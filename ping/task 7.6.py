from scapy.all import *


def get_address():
    dest_ip = input('What is the destination address? ')
    return dest_ip


def build_packet(dst_ip):
    ping_packet = IP(dst = dst_ip)/ICMP(type = 'echo-request')
    return ping_packet

def send_packet(ping_packet):
    ping_responses = []
    number_of_packets = int(input('How many ping requests do you want to send? '))
    print('Sending ' + str(number_of_packets) + ' packets')
    for x in range(number_of_packets):
        ping_packet[ICMP].id = x
        ping_response = sr1(ping_packet, verbose = 0)
        ping_responses.append(ping_response)
    return ping_responses, number_of_packets

def show_responses(ping_responses, number_of_packets):
    responses_num = len(ping_responses)
    lost_num = number_of_packets - responses_num

    print('Recieved: ' + str(responses_num) + ' Packets')
    print('Lost: ' + str(lost_num) + ' Packets')
    print('\n*************\n')

    answer = input('Do you want to see the packets? ')

    if answer == 'yes':
        for packet in ping_responses:
            print(packet.summary())
    else:
        pass

def main():
    dest_ip = get_address()
    ping_packet = build_packet(dest_ip)
    ping_responses, number_of_packets = send_packet(ping_packet)
    show_responses(ping_responses, number_of_packets)

if __name__ == '__main__':
    main()