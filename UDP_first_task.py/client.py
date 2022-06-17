import socket
import time


# Making the UDP client
UDP_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
start_time = time.time()

# Sending packets
UDP_client.sendto('almog'.encode(), ('127.0.0.1', 8821))

# Recieving packets
(data, remote_address) = UDP_client.recvfrom(1024)

# Printing the data
print('The server send: ' + data.decode())
end_time = time.time()

print(end_time - start_time)

# Closing the client
UDP_client.close()
