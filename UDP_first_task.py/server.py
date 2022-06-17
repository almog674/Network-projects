import socket

UDP_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_server.bind(('0.0.0.0', 8821))
(UDP_client, client_address) = UDP_server.recvfrom(1024)

data = UDP_client.decode()
response = data + ' Hello'
UDP_server.sendto(response.encode(), client_address)

UDP_server.close()