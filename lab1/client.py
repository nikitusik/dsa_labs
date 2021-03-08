import socket

client = socket.socket()
host = socket.gethostname()
port = 12345

client.connect((host, port))
file = open('cat.png', 'rb')
print('Sending...')
data = file.read(2048)

while (data):
    client.send(data)
    data = file.read(2048)

print("Done Sending")
file.close()
client.close()
print("Close client")