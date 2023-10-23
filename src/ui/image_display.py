import logging
from typing import Optional
from pathlib import Path
from PIL import Image, ImageQt
from PySide6 import QtGui
from PySide6.QtGui import QImage


class ImageDisplayer:
    
    def __init__(self, image_path: str = '/Users/azusa/research/project/RemoteDetector/resources/images'):
        self.image_files = self.load_images(image_path)
        self.image_index: int = 0

    @staticmethod
    def load_images(image_path: str):
        image_path = Path(image_path)
        supported_suffix = ['.jpeg', '.png', '.jpg']
        image_files = [str(i)for i in image_path.iterdir()
                       if i.suffix in supported_suffix]
        return image_files

    def get_image(self, is_next: [-1, 0, 1], w_box: int | float, h_box: int | float):
        self.change_index(is_next)
        self.image_showing = Image.open(self.image_files[self.image_index])
        print('is_changed')
        # image_qt = ImageQt.fromqimage(image)
        image_qt = ImageQt.ImageQt(self.image_showing)
        image_qt = self.image_resize(image_qt, w_box, h_box)
        # image_q = QImage('/Users/azusa/research/azusa_dataset/z_非常棒的检测结果/IMG_0647.jpeg')

        return image_qt

    @staticmethod
    def image_resize(image: QImage, w_box, h_box):
        w, h = image.width(), image.height()
        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return image.scaled(width, height)

    def change_index(self, is_next: [-1, 0, 1] = 0):
        if is_next == 1:
            if self.image_index == len(self.image_files) - 1:
                self.image_index = 0
            else:
                self.image_index += 1
        elif is_next == -1:
            if self.image_index == 0:
                self.image_index = len(self.image_files) - 1
            else:
                self.image_index -= 1
        else:
            pass




if __name__ == '__main__':
    imageDisplayer = ImageDisplayer
    imageDisplayer.get_image()
