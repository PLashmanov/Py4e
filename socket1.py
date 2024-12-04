import socket

# Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at 'data.pr4e.org' on port 80 (HTTP)
mysock.connect(('data.pr4e.org', 80))

# Send the GET request for the desired file
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# Receive the response and print it
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket
mysock.close()