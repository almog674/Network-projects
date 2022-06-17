## Real server
import socket

class Server:
    response_codes = {'good': '200 OK', 'not found': '404 Not Found'}

    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        http_server = self.initialize_server(self.IP, self.PORT)
        http_client = self.handle_client(http_server)
        message_split = self.handle_request(http_server, http_client)
        page_requested, request_type = self.validate_request(message_split)
        if request_type == 'GET':
            pass
        elif request_type == 'POST':
            pass


    def initialize_server(self, IP, PORT):
        http_server = socket.socket()
        http_server.bind((IP, PORT))
        http_server.listen()
        print('The server is up and ready!!')
        return http_server


    def handle_client(self, http_server):
        http_client, client_address = http_server.accept()
        print('Client connected!!' + str(client_address))
        return http_client


    def handle_request(self, http_server, http_client):
        message = http_client.recv(1024).decode()
        message_split = message.split(sep="\n")
        print(message_split)
        return message_split


    def validate_request(self, message_split):
        message_header = message_split[0]
        message_header_split = message_header.split(sep=' ')

        message_type = message_header_split[0]
        message_page_requested = message_header_split[1]
        message_protocol = message_header_split[2]

        if (message_type == 'GET' or message_type == 'POST')  and 'HTTP/1.1' in message_protocol and len(message_header_split) == 3:
            # print('valid request')
            pass
        else:
            print('unvalid request')
            self.close_connection()
        return (message_page_requested, message_type)
    
    def send_data()





almog = Server('0.0.0.0', 8080)
