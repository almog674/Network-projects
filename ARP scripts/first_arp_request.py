from scapy.all import *


DEFAULT_GATEWAY_ADDRESS = '8c:59:c3:b2:84:28'


def main():
    my_packet = Ether(dst = 'ff:ff:ff:ff:ff:ff')/IP(dst = '10.100.102.1')/ICMP()
    sendp(my_packet)


if __name__ == "__main__":
    main()