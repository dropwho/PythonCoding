import socket
import ssl

target_host = "www.google.com"
target_port = 443

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Create a default SSL context
context = ssl.create_default_context()

try:
    # Wrap the socket with SSL for HTTPS
    wrapped_socket = context.wrap_socket(client, server_hostname=target_host)

    # Connect the client
    wrapped_socket.connect((target_host, target_port))

    # Send some data (HTTP request)
    wrapped_socket.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

    # Receive some data (HTTP response)
    response = wrapped_socket.recv(4096)

    print(response.decode())
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    wrapped_socket.close()
