import socket
import os

def handle_request(request):
    # Extract the filename from the request
    filename = request.split()[1]

    # If the filename is empty, serve the index.html file
    if filename == "/":
        filename = "/index.html"

    # Try to open the file
    try:
        with open("." + filename, "rb") as f:
            content = f.read()
            status = "200 OK"
    except FileNotFoundError:
        content = b"<h1>404 Not Found</h1>"
        status = "404 Not Found"

    # Build the response message
    response = f"HTTP/1.1 {status}\r\nContent-Length: {len(content)}\r\n\r\n".encode() + content

    return response

def start_server() -> object:
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a public host and port
    server_socket.bind(('localhost', 6789))

    # Listen for incoming connections
    server_socket.listen()

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()

        # Receive the request
        request = client_socket.recv(1024).decode()

        # Handle the request
        response = handle_request(request)

        # Send the response
        client_socket.sendall(response)

        # Close the connection
        client_socket.close()

if __name__ == '__main__':
    start_server()
