from scapy.all import *

MY_MAC = '50:65:f3:2f:79:0b'

def ethernet_filter(frame):
    return (Ether in frame) and (frame[Ether].dst == MY_MAC)

def print_address(frame):
    print(frame[Ether].dst)

frames = sniff(count = 10, lfilter = ethernet_filter, prn = print_address)


