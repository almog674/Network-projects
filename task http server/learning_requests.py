import requests

# # Send a get requests for a web page
# r = requests.get('https://he.wikipedia.org/wiki/%D7%99%D7%A9%D7%A8%D7%90%D7%9C')
# print(r.text)

# # Download image
# r = requests.get('https://www.sport5.co.il/Sip_Storage/FILES/9/1054079.jpg')
# with open('cave.jpg', 'wb') as  f:
#     f.write(r.content)

## Check if the response is valid 
# print(r.ok)

# # Post request
# payload = {'username': 'almog67', 'password': 'almog60'}
# r = requests.post('https://httpbin.org/post', data=payload)

# r_dict = r.json()

# print(r_dict['form']['username'])

# r = requests.get('https://www.sport5.co.il/Sip_Storage/FILES/9/1054079.jpg')
# f = open('cave.jpg', 'wb')
# f.write(r.content)
# f_for_read = open('cave.jpg', 'rb')

# payload = {'data': f_for_read}
# response = requests.post('http://127.0.0.1:8080/', data=payload)

# r_dict = r.json()

# f.close()


