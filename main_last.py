import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QFormLayout
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
from src.ui.smoke_detector_ui import Ui_MainWindow
from PIL import Image
from pathlib import Path
from time import strftime
import logging
import yaml

"""
1. 首先实现一个阳间的照片查看器
2. 来自服务器的消息监视器
"""


class MainWindow(QMainWindow):
    def __init__(self, resources_path:str ,*args, **kwargs):
        super().__init__()
        logging.debug(f'resources_path: {resources_path}')
        self.resources_path = Path(resources_path)
        self.image_files = self.load_images(
            self.resources_path/"images")  # 静态load
        self.initui()  # 初始化ui
        self.image_index = 0
        self.display_image(self.image_files[self.image_index])
        self.ImageSelectorBind()

    def initui(self,):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def load_images(self, image_path: Path | str):
        supported_suffix = ['.jpeg', '.png', '.jpg']
        image_files = [str(i)for i in image_path.iterdir()
                       if i.suffix in supported_suffix]
        return image_files

    def display_image(self, image_file: str, scaling_ratio: float = 0.8):

        self.pil_iamge = QImage(image_file)

        def display2screen(self: MainWindow, image):
            image = self.image_resize(self.width(), self.height(), self.pil_iamge)
            pixmap = QPixmap.fromImage(image)
            self.ui.ImageDisplayer.resize(
                image.width()*scaling_ratio, image.height()*scaling_ratio)
            self.ui.ImageDisplayer.setPixmap(pixmap)
        display2screen(self=self, image=self.pil_iamge)
    

        # 随时间刷新part
        # self.timer = QTimer(self)  # 定义定时器，用于控制显示视频的帧率
        # self.timer.timeout.connect(
        #     lambda: display2screen(self, self.pil_iamge))
        # self.timer.start(10)

    def image_resize(self, w_box, h_box, pil_image: QImage):  # 参数是：要适应的窗口宽、高、Image.open后的图片
        w, h = pil_image.width(), pil_image.height()  # 获取图像的原始大小
        f1 = 1.0*w_box/w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        # return pil_image.resize(width, height)
        return pil_image.scaled(width, height)

    def ImageSelectorBind(self,):
        self.ui.NextImageButton.clicked.connect(lambda: self.display_image(
            image_file=self.image_files[self.get_iamge_index(is_next=True)]))

        self.ui.LastImageButton.clicked.connect(lambda: self.display_image(
            image_file=self.image_files[self.get_iamge_index(is_next=False)]))
        # self.ui.NextImageButton.clicked.connect(lambda:print('12323'))

    def get_iamge_index(self, is_next: bool = True):
        if is_next:
            if self.image_index == len(self.image_files) - 1:
                self.image_index = 0
            else:
                self.image_index += 1
        else:
            if self.image_index == 0:
                self.image_index = len(self.image_files) - 1
            else:
                self.image_index -= 1

        return self.image_index


def logging_setting(log_path):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S',
                        handlers=[logging.FileHandler(log_path),
                                  logging.StreamHandler(sys.stdout)]
                        )

    logging.info(f'Logging Server Start!')


def main(config: str):
    with open(config, 'r') as f:
        config: dict = yaml.safe_load(f)
    print(config)
    logging_setting(config.get('log_path'))
    app = QApplication(sys.argv)
    window = MainWindow(config.get('resources_path'),config)
    window.show()
    sys.exit(app.exec())




if __name__ == '__main__':
    config = 'resources/config.yml'
    main(config)
    # main(config)
