from scapy.all import *

dns_packet = IP(dst = '8.8.8.8')/UDP(sport = 33333, dport = 53)/DNS(qdcount = 1)/DNSQR(qname = 'www.google.com')
response = sr1(dns_packet)



