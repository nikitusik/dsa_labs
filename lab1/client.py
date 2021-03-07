import socket  # Import socket module

client = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.

client.connect((host, port))
file = open('cat.jpg', 'rb')
print('Sending...')
data = file.read(2048)

while (data):
    print('Sending...')
    client.send(data)
    data = file.read(2048)

print("Done Sending")
file.close()
client.close()  # Close the socket when done
