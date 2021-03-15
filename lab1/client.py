import socket
import os

from lab1.util import int_to_bytes

client = socket.socket()
host = socket.gethostname()
port = 12345

client.connect((host, port))
size = int_to_bytes(os.path.getsize('cat.png'))
client.send(size)

file = open('cat.png', 'rb')
print('Sending...')

data = file.read(2048)
while (data):
    client.send(data)
    data = file.read(2048)


file.close()


print("Done Sending")

client.close()
print("Close client")