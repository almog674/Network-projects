from scapy.all import *


def get_domain():
    domain = input('Put a domain here and get the IP address: ')
    return domain

def make_packet(domain):
    packet = IP(dst = '10.100.102.1')/UDP(sport = 44444, dport = 53)/DNS(qdcount = 1)/DNSQR(qname = domain)
    return packet
    
def send_packet(packet):
    response = sr1(packet)
    return response

def clear_response(response):
    response_clear = response[DNSRR]
    print(response_clear.show())
    return response_clear

def get_IP_from_response(response_clear):
    if type(response_clear.rdata) == str:
        return response_clear.rdata
    else:
        new_domain = response_clear.rdata.decode()
        return get_IP(new_domain)


def get_IP(domain):
    packet = make_packet(domain)
    response = send_packet(packet)
    response_clear = clear_response(response)
    IP = get_IP_from_response(response_clear)
    return IP

    
def main():
    domain = get_domain()
    IP = get_IP(domain)
    print(IP)
    
if __name__ == '__main__':
    main()