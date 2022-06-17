from scapy.all import *


# packet_for_google = IP(dst = '8.8.8.8')/TCP()/Raw('Hello')
# send(packet_for_google)
# print(packet_for_google.show()) 

def facebook_filter(packet):
    return (packet[IP].dst == '157.240.20.35')

def print_packets(packet):
    print(packet.show())

facebook_packets = sniff(count = 5, lfilter = facebook_filter, prn = print_packets)