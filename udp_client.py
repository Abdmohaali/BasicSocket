import socket

HOST = ""  # todo: specify the server's hostname or IP address inside the quotes
PORT = 22 # todo: specify the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    pass_in = input("Type a message you want relayed:")
    while pass_in != "done":
        message = format(pass_in)
        byte_msg = message.encode('utf-8')
        s.sendall(byte_msg)
        data = s.recv(1024)

print("Received: {}".format(data.decode('utf-8')))