class ImageData:
    def __init__(self, image_size: tuple, image_mode: str, image_bytes: bytes):
        self.image_size: tuple = image_size
        self.image_mode: str = image_mode
        self.iamge_bytes: bytes = image_bytes