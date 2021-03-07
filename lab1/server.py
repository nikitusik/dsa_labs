import socket  # Import socket module

server = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
server.bind((host, port))  # Bind to the port
file = open('server_cat.jpg', 'wb')
server.listen()  # Now wait for client connection.
while True:
    client_socket, client_addr = server.accept()  # Establish connection with client.
    print('Got connection from', client_addr)
    print("Receiving...")
    data = client_socket.recv(2048)
    while (data):
        print("Receiving...")
        file.write(data)
        data = client_socket.recv(2048)
    file.close()
    print("Done Receiving")
    client_socket.close()
