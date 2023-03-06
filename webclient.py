import sys
from socket import *

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_host, server_port))
request = 'GET /{} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(filename, server_host)
client_socket.send(request.encode())
response = ''
while True:
    recv_data = client_socket.recv(1024).decode()
    if not recv_data:
        break
    response += recv_data
print(response)
client_socket.close()
