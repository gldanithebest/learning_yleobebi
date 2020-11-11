import socket

HOST = '192.168.88.241'  # The server's hostname or IP address
PORT = 1234        # The port used by the server
something = ''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while something!= 'esc'.encode('utf-8'):
        something= input('Your messagge:').encode('utf-8')
        s.sendall(something)
        data = s.recv(1024)
        print(data.decode('utf-8'))


print('Received: ', repr(data))