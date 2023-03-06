import socket
import sys

def make_request(server_host, server_port, filename):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Build the request message
    request = f"GET {filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n".encode()

    # Send the request
    client_socket.sendall(request)

    # Receive the response
    response = client_socket.recv(1024)

    # Close the connection
    client_socket.close()

    return response

if __name__ == '__main__':
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    response = make_request(server_host, server_port, filename)
    print(response.decode())
