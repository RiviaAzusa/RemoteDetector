import socket

frp_server_host = '10.23.127.255'
frp_server_port = 6010  # FRP服务器的端口号

# 创建一个TCP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 连接到FRP服务器
    a = client_socket.connect((frp_server_host, frp_server_port))
    print(a)
    # 现在，您可以通过client_socket与FRP服务器通信
    # 例如，向FRP服务器发送数据
    data_to_send = "Hello, FRP Server!"
    client_socket.send(data_to_send.encode())

    # 接收从FRP服务器返回的数据
    received_data = client_socket.recv(1024)
    print("Received data from FRP Server:", received_data.decode())


except Exception as e:
    print("Error:", e)

finally:
    # 关闭套接字连接
    client_socket.close()
