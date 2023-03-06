import socket
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = int(sys.argv[2])
FILE_PATH = sys.argv[3]

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

request_data = f'GET {FILE_PATH} HTTP/1.1\r\n'
request_data += f'Host: {SERVER_HOST}\r\n'
request_data += 'Connection: close\r\n\r\n'

client_socket.send(request_data.encode())

response_data = client_socket.recv(1024).decode()
print(response_data)

client_socket.close()
