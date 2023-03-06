import socket
import os
import threading

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

def handle_connection(client_socket, client_address):
    # Receive the request
    request = client_socket.recv(1024).decode()

    # Handle the request
    response = handle_request
