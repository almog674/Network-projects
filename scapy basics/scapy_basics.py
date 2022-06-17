from scapy.all import *


def dns_filter(packets):
    return (DNS in packets and packets[DNS].opcode == 0 and packets[DNSQR].qtype == 1)

def print_query(dns_packets):
    print(dns_packets[DNSQR].qname)

packets = sniff(count = 10, lfilter = dns_filter, prn = print_query)
packet_example = packets[4]
packet_example = packet_example[DNSQR]
packet_example.show()