from scapy.all import *

def make_packet(port):
    syn_segment = TCP(dport = port, seq = 123, flags = 'S')
    syn_packet = IP(dst = 'google.com')/syn_segment
    return syn_packet

def send_packets(syn_packet):
    response = send(syn_packet)
    return response

def main():
    ports = []
    for port in range(80):
        syn_packet = make_packet(port)
        response = send_packets(syn_packet)
        if response != None:
            ports.append(port)
        else:
            pass
    print(ports)
    

if __name__ == '__main__':
    main()