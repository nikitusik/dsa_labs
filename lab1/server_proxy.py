import socket
import numpy as np
import cv2
import random


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


proxy = socket.socket()
host = socket.gethostname()
port_client = 12345
port_server = 12346
proxy.bind((host, port_client))
file = open('proxy_noise_cat.png', 'wb')
proxy.listen()

client_socket, client_addr = proxy.accept()
print('Got connection from', client_addr)
print("Receiving...")
data = client_socket.recv(2048)
while (data):
    file.write(data)
    data = client_socket.recv(2048)

print("Done Receiving")

file.close()
client_socket.close()
proxy.close()

print("Add noise salt and pepper")
image = cv2.imread("proxy_noise_cat.png")
noise_img = sp_noise(image, 0.005)
cv2.imwrite("proxy_noise_cat.png", noise_img)
print("Done add noise")

proxy = socket.socket()
proxy.connect((host, port_server))
file = open('proxy_noise_cat.png', 'rb')

print('Sending...')
data = file.read(2048)

while (data):
    proxy.send(data)
    data = file.read(2048)

print("Done Sending")
file.close()
proxy.close()
print("Close server proxy")