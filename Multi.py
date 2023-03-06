import sys
from socket import *

server_host = 'localhost'
server_port = 6789
filename = 'index.html'
bot_socket = socket(AF_INET, SOCK_STREAM)
bot_socket.connect((server_host, server_port))
request = 'GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(filename, server_host)
bot_socket.send(request.encode())
response = bot_socket.recv(1024).decode()
if '200 OK' in response:
    print('The web server is running properly.')
else:
    print('There is something wrong with the web server.')
bot_socket.close()
