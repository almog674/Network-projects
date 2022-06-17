from scapy.all import *

# my_packet = IP(dst = '8.8.8.8', ttl =)
# my_packet.show()

my_packet = Ether()/IP(ttl = 4)/TCP(dport = 80)/Raw('GET / HTTP\\1.0\r\n')
print(hexdump(my_packet))