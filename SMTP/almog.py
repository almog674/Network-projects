import smtplib, ssl

# Global Variables
gmail_user = 'almogmaimon674@gmail.com'
gmail_password = input(str('What is your password: '))

mail_from = 'almogmaimon674@gmail.com'
mail_to = 'eliyaomaz@gmail.com'
subject = 'I Love You...'
message = open('email data', 'r', encoding='utf-8')
message_content = message.read()
print(message_content)
message_content = message_content + '\n\rEmail Delivered Successfuly!!\nSent fully automaticly with python Bot'

message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (mail_from, ", ".join(mail_to), subject, message_content)

server = smtplib.SMTP('108.177.15.108', 587)
server.starttls()
server.login(gmail_user, gmail_password)
print('Client Connected!!')
server.sendmail(mail_from, mail_to, message)
print('Email send!!')