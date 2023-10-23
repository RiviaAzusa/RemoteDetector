import yaml
from main_last import logging_setting
import argparse


def file_manager_test():
    from server_part.file_manager import FileManager
    a = FileManager('resources')


def time_test():
    import time
    print(time.strftime("%Y-%m-%d %H:%M:%S"))


def yaml_test():
    import yaml
    with open('resources/config.yml', 'r') as f:
        data = yaml.safe_load(f)
        print(data)


def test_server(config: str = 'resources/config.yml'):
    from server_part.tcp_server import PredictorServer
    with open(config, 'r') as f:
        config: dict = yaml.safe_load(f)
    print(config)
    logging_setting(config.get('log_path'))
    app = PredictorServer()
    app.run()


def test_client(config: str = 'resources/config.yml'):
    from server_part.tcp_client import PredictorClient
    with open(config, 'r') as f:
        config: dict = yaml.safe_load(f)
    print(config)
    logging_setting(config.get('log_path'))
    app = PredictorClient()
    app.run()

class ImageData:
    def __init__(self, image_size: tuple, image_mode: str, image_bytes: bytes):
        self.image_size: tuple = image_size
        self.image_mode: str = image_mode
        self.iamge_bytes: bytes = image_bytes


def test_image():
    from PIL import Image
    from io import BytesIO
    import pickle

    image = Image.open('resources/images/1533577358_+00900.jpg')
    image_size = image.size
    image_mode = image.mode
    image_bytes = image.tobytes()
    image_data = ImageData(image_size, image_mode, image_bytes)
    total_bytes = pickle.dumps(image_data)
    recv_bytes: ImageData = pickle.loads(total_bytes)
    # image_ = Image.frombytes(image_mode, image_size, image_bytes)
    print(recv_bytes.image_size, recv_bytes.image_mode)
    print(type(recv_bytes.image_size))
    image_ = Image.frombytes(size=recv_bytes.image_size,
                             mode=recv_bytes.image_mode,
                             data=recv_bytes.iamge_bytes)

    image_.show()

def test_image_():
    from PIL import Image
    from io import BytesIO
    import pickle

    image = Image.open('resources/images/1533577358_+00900.jpg')
    print(type(image))
    image_bytes = BytesIO()
    image.save(image_bytes,format='JPEG')
    print(type(image_bytes.getvalue()))
    b = image_bytes.getvalue()
    print(len(b))
    b = b +b'wdnmd'
    b = b[:-5]
    image_ = Image.open(b)
    image_.show()

from typing import Optional
def type_test(a):
    print(bool(a))
    bool(a is None)

def type_test_(): 
    type_test(True)
    type_test(False)
    type_test(None)

if __name__ == '__main__':
    type_test_()
    # test_image_()
    # test_image_()
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-c','--client',action='store_true',default=False)
    # args = parser.parse_args()
    # if args.client:
    #     print('This is client')
    #     test_client()
    # else:
    #     print('This is server')
    #     test_server()
