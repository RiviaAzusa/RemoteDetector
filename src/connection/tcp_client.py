import socket
import sys
import pickle
from PIL import Image
from io import BytesIO
import time
import logging

# from server_part.base import ImageData




class PredictorClient:
    def __init__(self, host='localhost', port=11251):
        self.socket_connector = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        logging.info((f'try to connet with host:{host} port:{port}'))
        self.socket_connector.connect((host, port))
        logging.info(f'successful connecting with host:{host} port:{port}')

    def run(self):
        file = '/Users/azusa/research/project/smoke_detector/resources/images/1533577358_+00900.jpg'
        image_data = self.image_precesser(file)
        print(len(image_data))
        image_data += b'endsign'
        logging.info('sending image data')
        self.socket_connector.send(image_data)
        logging.info('sending over, recv the result')
        result = self.socket_connector.recv(1024)
        result = pickle.loads(result)
        print(result)
    
    @staticmethod
    def image_precesser(file: str):
        image = Image.open(file)
        image_bytes = BytesIO()
        image.save(image_bytes,format='JPEG')
    
        return image_bytes.getvalue()
    


if __name__ == '__main__':
    # server_host = '8.137.11.223'
    # server_port = 11451
    # app = PredictorClient(server_host,server_port)
    app = PredictorClient()
    app.run()
