import socket

HOST = "10.0.0.1"  #
PORT = 1500 #

# open a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print('Server listening on {}:{}'.format(HOST, PORT))
    while True:
        data, addr = s.recvfrom(1024)
        if not data:
            break
        original_message = data.decode('utf-8')
        s.sendto(original_message.upper().encode('utf-8'), addr)