import socket
import selectors
import logging
import pickle

from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from io import BytesIO
from random import randint
from re import search
from typing import Optional


class SingleImageReceiver:
    def __init__(self, end_sign: bytes = b'endsign'):
        self.image: bytes = b''
        self.end_sign = end_sign


    def check(self, data_segment: bytes):
        res = search(self.end_sign, data_segment)
        if bool(res):
            self.image += data_segment[:res.span()[0]]
            return True
        else:
            self.image +=data_segment
            return False

    def getimg(self) -> JpegImageFile:
        print(len(self.image))
        return Image.open(BytesIO(self.image))
    


class PredictorServer:
    def __init__(self, host='localhost', port=11251):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.serversocket = socket.socket()
        self.serversocket.bind((host, port))
        self.serversocket.listen(5)
        self.serversocket.setblocking(False)
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.serversocket, selectors.EVENT_READ, self.accept)

        self.image_receiver = SingleImageReceiver()
        self.image:Optional(JpegImageFile) = None
        self.times = 0

    def run(self,):
        while True:
            events = self.sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj, mask)

    def accept(self, sock: socket.socket, mask):
        conn, addr = sock.accept()
        logging.info(f'accepted: {repr(conn)} from: {repr(addr)}')
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)

    def read(self, conn: socket.socket, mask):
        data = conn.recv(1024)
        if data:
            self.times +=1
            logging.info(f'successful receive {repr(data[:10])} from {conn}')
            ans = self.image_receiver.check(data)
            if ans:
                print(f'find it at {self.times}th')
                self.image = self.image_receiver.getimg()
                conn.send(self.predict_image(self.image))

                self.sel.unregister(conn)
                conn.close()  # 关闭此次连接
        else:
            logging.info(f'No data, closing: {conn}')
            self.sel.unregister(conn)
            conn.close()  # 关闭此次连接


    @staticmethod
    def predict_image(image: JpegImageFile):
        print(image.size)
        w, h = image.size
        def gen_random_result():
            x1 = randint(0, w-200)
            x2 = x1 + randint(0, 200)
            y1 = randint(0, h-200)
            y2 = y1 + randint(0, 200)
            return [x1, y1, x2, y2]

        return pickle.dumps([gen_random_result() for i in range(3)])


if __name__ == '__main__':
    app = PredictorServer()
    app.run()
