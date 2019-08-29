import socket
s = socket.socket()
s.connect(('127.0.0.1', 2000)) # local host in this case (127.0.0.1) and port 2000
print("Recieved:", s.recv(1024).decode()) # accept 1024 bytes of data
s.close()