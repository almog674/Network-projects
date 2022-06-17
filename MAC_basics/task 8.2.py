from scapy.all import *

addresses_list = []
MY_MAC = '50:65:f3:2f:79:0b'

def ethernet_filter(frame):
    return (Ether in frame) and (frame[Ether].dst == MY_MAC)

def print_address(frame):
    for el in addresses_list:
        if frame[Ether].src == el:
            return
    addresses_list.append(frame[Ether].src)
    print(frame[Ether].src)

frames = sniff(count = 100, lfilter = ethernet_filter, prn = print_address)
print(addresses_list)