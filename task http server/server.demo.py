# # Demo server
import socket
import sys
import requests




class Authentication_Database:
    def __init__(self, users):
        self.users = users

    def delete_user(self):
        pass

    def add_user(self, username, level):
        # new_user = {'username': username.username, 'password': username.password}
        new_user = username
        self.users[username.username] = new_user
        print(self.users)

    def show_data(self):
        pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.level = self.check_level()
        self.info = self.get_user_commands

    def check_level(self):
        if self.username == 'almog67' and self.password == 'almog60':
            return 'admin'
        else:
            return 'user'
    
    def get_user_commands(self):
        user_info = 'Your username is: ' + self.username + '\n\rYour password is: ' + self.password + '\n\rYour level is: ' + self.level + '\n\r\n\r'
        if self.level == 'user':
            commands = 'Your options are:\n\r1. Get Next Number\n\r2. Calculate Area\n\r3. Go To Home Page'
        elif self.level == 'admin':
            commands = 'Your options are:\n\r1. Get Next Number\n\r2. Calculate Area\n\r3. Go To Home Page\n\r4. Show Database\n\r5. Delete User'

        data = user_info + commands
        print(data)
        return data

almog674 = User('almog67', 'almog60')
eliyaomaz = User('eliyaomaz', 'eliyaomaz123')


users_begin = {almog674.username: almog674, eliyaomaz.username: eliyaomaz}
auth_database = Authentication_Database(users_begin)



class Server:

    response_codes = {'good': '200 OK', 'not_found': '404 Not Found', 'unknown action': '500 Internal Server Error'}
    SOCKET_TIMEOUT = 10000

    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
        http_server = self.initialize_server(self.IP, self.PORT)
        while True:
            http_client = self.handle_client(http_server)
            http_client.settimeout(self.SOCKET_TIMEOUT)
            message_split = self.handle_request(http_server, http_client)
            page_requested = self.validate_request(message_split)
            response_data, data_type, data_size = self.send_data(page_requested, http_client, message_split)
            content = self.build_response(response_data, self.response_codes, http_server, data_type, data_size)
            self.send_full_response(content, http_client)
        self.close_connection(http_client, http_server)
        
    def read_file(self, path):
        data_file = open(path, 'r', encoding='utf-8')
        data = data_file.read()
        data_file.close()

        return data

    def read_image(self, path):
        image = open(path, 'rb')
        image_data = image.read()
        print('Memory size is: ' + str(sys.getsizeof(image_data)))
        image_data_size = str(sys.getsizeof(image_data) - 49)
        image.close()

        return image_data, image_data_size


    def get_next_number(self, page_requested):
        parameter = page_requested.find('=')
        parameter = page_requested[(parameter + 1)::]
        question = page_requested.find('?num=')
        if question != (-1) and parameter.isdigit():
            parameter = int(parameter)
            data = parameter + 1
        else:
            data = self.response_codes['unknown action']
        return str(data)

    def seperate_parameters_for_calculator(self, page_requested):
        # Seperate the task form the address
        page_requested_split = page_requested.split(sep='?', maxsplit=1)
        # Get the task
        parameter_container = page_requested_split[1]
        # Seperate the parameters
        parameter_container_split = parameter_container.split(sep='&')
        # Seperate the values
        shape = parameter_container_split[0].split(sep='=')
        shape = shape[1]
        width = parameter_container_split[1].split(sep='=')
        width = width[1]
        height = parameter_container_split[2].split(sep='=')
        height = height[1]

        print(width, shape, height)
        return (parameter_container, parameter_container_split, shape, width, height)


    def validate_request_for_calculater(self, page_requested, container_split):
        if container_split[0].find('shape=') != (-1) and container_split[1].find('width=') != (-1) and container_split[2].find('height=') != (-1):
            if page_requested.find('?') != (-1) and len(container_split) == 3:
                valid = 'yes'
                error_message = ''
            else:
                valid = 'no'
                error_message = self.response_codes['not found'] + '\n\rThe question dont spell good!'
        else:
            valid = 'no'
            error_message = self.response_codes['unknown action'] + '\n\rCheck Your parameters!'
        return (valid, error_message)
            
        

    def get_area(self, page_requested):
        # seperate_parameters
        (container, container_split, shape, width, height) = self.seperate_parameters_for_calculator(page_requested)
        # validate_request
        (valid, error_message) = self.validate_request_for_calculater(page_requested, container_split)
        if valid == 'yes':
            # calculate_area
            new_shape = Area_Calculator(shape, width, height)
            return (new_shape.area)
        else:
            return error_message

    def seperate_parameters(self, page_requested):
        parameters = []
        page_requested_split = page_requested.split(sep='?', maxsplit=1)
        parameter_container = page_requested_split[1]
        parameter_container_split = parameter_container.split(sep='&')
        for element in range(len(parameter_container_split)):
            parameter_clean = parameter_container_split[element].split(sep='=')
            parameter_clean = parameter_clean[1]
            parameters.append(parameter_clean)
        return parameters, parameter_container_split



    def validate_request_for_auth(self, parameters, parameter_container_split, page_requested):
        if parameter_container_split[0].find('username=') != (-1) and parameter_container_split[1].find('password=') != (-1):
            if page_requested.find('?') != (-1) and len(parameter_container_split) == 2:
                valid = 'yes'
                error_message = ''
            else:
                valid = 'no'
                error_message = self.response_codes['not found'] + '\n\rThe question dont spell good!'
        else:
            valid = 'no'
            error_message = self.response_codes['unknown action'] + '\n\rCheck Your parameters!'
        return (valid, error_message)


    def validate_parameters_for_auth(self, username, password, state):
        if state == 'sign_up':
            if username in auth_database.users.keys():
                valid = 'no'
                error_message = 'The username is not available'
            elif len(password) < 8 or username == password:
                valid = 'no'
                error_message = 'Ilegal password, the password has to be\n\r1. Not the same as the username\n\r2. at least 8 character long'
            else:
                valid = 'yes'
                error_message = ''
        else:
            if username not in auth_database.users.keys():
                valid = 'no'
                error_message = 'The username not existing'
            elif auth_database.users[username].password != password:
                valid = 'no'
                error_message = 'Wrong Password'
            else:
                valid = 'yes'
                error_message = ''
            
        return valid, error_message


    def sign_up(self, page_requested):
        # http://127.0.0.1:8080/sign_up?username=almog67&password=almog60

        # Get the parameters
        parameters, parameter_container_split = self.seperate_parameters(page_requested)
        username = parameters[0]
        password = parameters[1]
        # Validate the request
        (valid_request, error_message_request) = self.validate_request_for_auth(parameters, parameter_container_split, page_requested)
        # Validate Username & Password
        (valid_parameters, error_parameters) = self.validate_parameters_for_auth(username, password, 'sign_up')
        if valid_request == 'no':
            return error_message_request
        elif valid_parameters == 'no':
            return error_parameters
        else:
            # Make a user
            username = User(username, password)
            user_level = username.level
            # Update the database dictionary
            auth_database.add_user(username, user_level)
            self.sign_in(page_requested) 
       
        


    def sign_in(self, page_requested):
        # Get the parameters
        parameters, parameter_container_split = self.seperate_parameters(page_requested)
        username = parameters[0]
        password = parameters[1]
        # Validate the request
        (valid_request, error_message_request) = self.validate_request_for_auth(parameters, parameter_container_split, page_requested)
        # Validate Username & Password
        (valid_parameters, error_parameters) = self.validate_parameters_for_auth(username, password, 'sign_in')
        if valid_request == 'no':
            return error_message_request
        elif valid_parameters == 'no':
            return error_parameters
        else:
            print('Signed in succssesfuly!!')
            return auth_database.users[username].info()


    def initialize_server(self, IP, PORT):
        http_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        http_server.bind((IP, PORT))
        http_server.listen()
        print('The server is up and ready!!')
        return http_server

    def handle_client(self, http_server):
        http_client, client_address = http_server.accept()
        # print('Client connected!!' + str(client_address))
        return http_client


    def handle_request(self, http_server, http_client):
        message = http_client.recv(1024).decode()
        message_split = message.split(sep="\n")
        return message_split


    def validate_request(self, message_split):
        message_header = message_split[0]
        message_header_split = message_header.split(sep=' ')

        message_type = message_header_split[0]
        message_page_requested = message_header_split[1]
        message_protocol = message_header_split[2]

        if (message_type == 'GET' or message_type == 'POST') and 'HTTP/1.1' in message_protocol and len(message_header_split) == 3:
            # print('valid request')
            pass
        else:
            print('unvalid request')
            self.close_connection()
        return message_page_requested


    def send_data(self, page_requested, http_client, message_split):
        data_size = ''
        if page_requested == '/':
            data = self.read_file('webroot\index.html')
            data_type = '(test/plain)'
        elif 'favicon.ico' in page_requested:
            data = self.read_image('webroot\imgs\\favicon.ico')
            data_type = '(image/jpeg)'
        elif 'css' in page_requested:
            data = self.read_file('webroot\css\doremon.css')
            data_type = '(text/css)'
        elif 'jpg' in page_requested or 'png' in page_requested or 'gif' in page_requested:
            (data, image_data_size) = self.read_image('webroot\imgs\\abstract.jpg')
            data_type = '(image/jpeg)'
            data_size = image_data_size
        elif 'js' in page_requested:
            data = self.read_file("webroot\\" + page_requested[1::])
            data_type = '(text/javascript; charset=UTF-8)'
        elif 'calculate-next' in page_requested:
            data = self.get_next_number(page_requested)
            data_type = '(test/plain)'
        elif 'calculate-area' in page_requested:
            data = self.get_area(page_requested)
            data_type = '(test/plain)'
        elif 'sign_up' in page_requested:
            data = self.sign_up(page_requested)
            data_type = '(test/plain)'
        elif 'sign_in' in page_requested:
            data = self.sign_in(page_requested)
            data_type = '(test/plain)'
        else:
            data = self.response_codes['not found']
            data_type = '(test/plain)'
            print(message_split)
        
        return str(data), data_type, data_size


    def build_response(self, data, response_codes, http_server, data_type, size):
        if 'image' in data_type:
            sub = 'Accept-Ranges: bytes\r\n'
            sub = sub + 'Context_Length: ' + str(sys.getsizeof('webroot\imgs\abstract.jpg')) + '\r\n'
            sub = sub + 'Context_Type: ' + '(image/jpeg)' + '\r\n\r\n'
        else:
            sub = 'Context_Length: ' + str(len(data)) + '\r\n\r\n'
        main = "HTTP/1.1 " + response_codes['good'] + ' ' + data_type + '\r\n'
        merge = main + sub + data
        # /p/CHBGPbaFksyCa40sUXH3HBl95UncVAfxhCwNQU0/
        # 327,680
        
        return merge


    def send_full_response(self, content, http_client):
        http_client.send(content.encode())


    def close_connection(self, http_client, http_server):
        http_client.close()
        http_server.close()
    

class Area_Calculator:
    def __init__(self, shape, height, width):
        self.shape = shape
        self.height = int(height)
        self.width = int(width)
        self.main()

    def main(self):
        if self.shape == 'triange':
            self.area = (self.height * self.width) / 2
        elif self.shape == 'squere' or 'rectangle':
            self.area = (self.height * self.width)
        elif self.shape == 'cicle':
            self.area = (3.14 * (self.width ** 2))






almog = Server('0.0.0.0', 8080)

