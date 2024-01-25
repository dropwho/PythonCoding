import socket

target_host = "0.0.0.0"
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data as a byte string
data_to_send = b"Hannah I love you!"
client.send(data_to_send)

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
