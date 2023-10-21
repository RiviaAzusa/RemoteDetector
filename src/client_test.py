import socket
import sys
import pickle
from PIL import Image
from io import BytesIO


class Client:
    def __init__(self, host, port):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print(f'try to connect with host:{host} port:{port}')

        self.clientsocket.connect((host, port))
        print(f'successful connecting with host:{host} port:{port}')


    def run(self):
        self.clientsocket.send('From Azusa!'.encode())


if __name__ == '__main__':
    server_host = '8.137.11.223'
    server_port = 11451
    app = Client(server_host, server_port)
    app.run()
