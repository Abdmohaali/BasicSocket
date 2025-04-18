import socket

HOST = "10.0.0.1"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 1500  #todo: specify the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Enter a message: ")
        if message == "done":
            break
        byte_msg = message.encode('utf-8')
        s.sendall(byte_msg)
        data = s.recv(1024)

        print("Received: {}".format(data.decode('utf-8')))