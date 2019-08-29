import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('',2000)) # '' meaning binding to any ip address and 2000 is the port 

server.listen(10) # 10 here means 10 connections can be queued at once (min = 1)
print("Waiting for conenction...")

while True:
   client, address = server.accept() # accepting connection to client
   client.send('hello_world'.encode()) # send data to client, encode converts data to bytes
   client.close() # close connection