import socket
import threading
import os

PORT = 6789
SERVER_HOST = '127.0.0.1'
WEB_ROOT = './www/'

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode()
    request_lines = request_data.split('\r\n')
    request_line = request_lines[0]
    request_method, path, protocol = request_line.split()

    if path == '/':
        path = '/index.html'

    file_path = WEB_ROOT + path
    if not os.path.exists(file_path):
        response_data = 'HTTP/1.1 404 Not Found\r\n'
        response_data += 'Content-Type: text/html\r\n'
        response_data += '\r\n'
        response_data += '<html><body><h1>404 Not Found</h1></body></html>'
    else:
        with open(file_path, 'r') as f:
            file_content = f.read()
            response_data = 'HTTP/1.1 200 OK\r\n'
            response_data += 'Content-Type: text/html\r\n'
            response_data += '\r\n'
            response_data += file_content

    client_socket.send(response_data.encode())
    client_socket.close()


def start_server():
    print(f'Starting server on {SERVER_HOST}:{PORT}')

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, PORT))
    server_socket.listen()

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Client connected from {client_address[0]}:{client_address[1]}')

        t = threading.Thread(target=handle_request, args=(client_socket,))
        t.start()


if __name__ == '__main__':
    start_server()
