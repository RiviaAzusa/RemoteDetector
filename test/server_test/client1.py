import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
client_socket.connect(("localhost",1234))
# print('连接')
# client_socket.send('client1'.encode())
# recv =  client_socket.recv(1024).decode()
# print(recv)
for i in range(100):
    client_socket.send(f'msg{i}'.encode())
    recv =  client_socket.recv(1024).decode()
    print(recv)
# recv =  client_socket.recv(1024).decode()
# print(recv)


# client_socket.send('client1'.encode())
# recv =  client_socket.recv(1024).decode()
# print(recv)

# client_socket.send('client1'.encode())
# recv =  client_socket.recv(1024).decode()
# print(recv)