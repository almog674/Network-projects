from scapy.all import *


print('almog')
def http_get_filter(packet):
    return (TCP in packet and Raw in packet and str(packet[Raw]).find('GET') != (-1) and str(packet[Raw]).find('HTTP') != (-1))


def http_print(http_packets):
    to_print = str(http_packets[Raw])
    to_print_split = to_print.split(sep=' ')
    referer = to_print.find('Referer')
    referer_full = to_print[referer:referer + 100]
    referer_split = referer_full.split(sep='/')
    url = referer_split[2]
    print(url)
    

packets = sniff(count = 12, lfilter = http_get_filter, prn = http_print)