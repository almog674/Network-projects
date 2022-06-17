# Tasks
# 1. Build TCP client that connecting to SMTP server at port 25
# 2. Send "HELO" message to the server
# 3. Send the source address to the server
# 4. Send the destionation address to the server
# 5. Send "DATA" message to the server
# 6. Send the data itself as mail to the server
# 7. Disconnect the server and finish the programm

# import socket

# class SMTP_Client:
#     def __init__(self, IP, PORT):
#         self.IP = IP
#         self.PORT = PORT
#         self.smtp_client = self.initialize_client(self.IP, self.PORT)

#     def initialize_client(self, IP, PORT):
#         smpt_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         smpt_client.connect((IP, PORT))
#         print('Client connected successfuly!!')
#         return smpt_client

# smtp_client = SMTP_Client('108.177.15.108', 8090)


import socket
import smtplib
import getpass
import ssl
gmail_user = 'almogmaimon674@gmail.com'
gmail_password = input(str('What is your password: '))

mail_from = 'almogmaimon674@gmail.com'
mail_to = 'eliyaomaz@gmail.com'
endmsg = "\r\n.\r\n"

mailServer = '108.177.126.109'
mailPort = 587


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("conectando el sooooocket")
# wrappedSocket = ssl.wrap_socket(clientSocket,      #Here we try to create a secure socket to that
#     ssl_version=ssl.PROTOCOL_TLSv1,     #the mail server makes a handshake and create the response
#     ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5",
#     cert_reqs=ssl.CERT_REQUIRED)

clientSocket.connect((mailServer, mailPort))



print ("Client Connected!!")
recv = clientSocket.recv(1024).decode()
#Fill in end
print ("Este es el recv: %s" % recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')




# Send HELO command and print server response.
heloCommand = ('HELO Alice\r\n')
print (heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print ("Este es el recv1: %s" % recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')


Username=input("Insert Username: ")
Password= getpass.getpass(prompt='Insert Password: ')


UP = ("\000"+Username+"\000"+Password)
UP = UP
print (UP)
UP = UP.strip("\n")
login = 'AUTH PLAIN '+ UP + '\r\n'
print (login)
clientSocket.send(login.encode())
recv_from_TLS = clientSocket.recv(1024)
print (recv_from_TLS)




# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM: <'+ Username+'>\r\n'
print (fromCommand)
clientSocket.send(fromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print ("Este es el recv2: %s" % recv2)
if recv2[:3] != '250':
    print('rcpt2 to 250 reply not received from server, cabron.')
# Fill in end

# Send RCPT TO command and print server response.

receiver =input("Send email to: ")
# Fill in start
toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
print (toCommand)
clientSocket.send(toCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print ("Este es el recv3: %s" % recv3)
if recv3[:3] != '250':
    print('rcpt3 to 250 reply not received from server, cabron.')

# Send DATA command and print server response.
# Fill in start

dataCommand = 'DATA\r\n'
print (dataCommand)
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024)
print (recv4)
Subject=input("Subject: ")
Text=input("Message: ")
message = "Subject: " + Subject + "\r\n\r\n" + Text + "\r\n" + endmsg + "\r\n"
clientSocket.send(message.encode())
recv5 = clientSocket.recv(1024).decode()
print (recv5)
#Fill in end


clientSocket.send("QUIT\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
print (recv6)
clientSocket.close()

#Fill in end
# © 2020 GitHub, Inc.
# Terms
# Privacy
# Security
# Status
# Help
# Contact GitHub
# Pricing
# API
# Training
# Blog
# About
