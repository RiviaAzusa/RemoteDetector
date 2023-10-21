import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect(("localhost",11251))

# client_socket.send('client2'.encode())
# client_socket.send('client2'.encode())
# client_socket.send('client2'.encode())
client_socket.send('client3'.encode())
recv =  client_socket.recv(1024).decode()
print(recv)

# client_socket.send('client2'.encode())
# recv =  client_socket.recv(1024).decode()
# print(recv)
# client_socket.send('client2'.encode())
# recv =  client_socket.recv(1024).decode()
# print(recv)