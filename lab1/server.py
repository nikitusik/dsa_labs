import socket
import cv2

server = socket.socket()
host = socket.gethostname()
port = 12346
server.bind((host, port))

server.listen()
while True:
    proxy_socket, proxy_addr = server.accept()
    print('Got connection from', proxy_addr)
    print("Receiving...")
    file = open('server_cat.png', 'wb')
    data = proxy_socket.recv(2048)
    while (data):
        file.write(data)
        data = proxy_socket.recv(2048)
    file.close()
    proxy_socket.close()
    print("Done Receiving")

    print("Start delete noise")
    image = cv2.imread("server_cat.png")
    median_blur = cv2.medianBlur(image, 5)
    cv2.imwrite("server_cat.png", median_blur)
    print("Done delete noise")

