import sys
import logging

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QImage, QPixmap, QResizeEvent

from .RemoteDetector_ui import Ui_MainWindow
from .image_display import ImageDisplayer


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)
        self.imageDisplayer = ImageDisplayer()
        self.ImageSelectorBind()
        self.display_image()
        

    def display_image(self, is_next=0):
        w_box = self.ImageLabel.width()
        h_box = self.ImageLabel.height()
        print(f'w_box:{w_box}, h_box:{h_box}')
        qimage = self.imageDisplayer.get_image(
            is_next=is_next, w_box=w_box, h_box=h_box)

        print(type(qimage))
        pixmap = QPixmap.fromImage(qimage)
        self.ImageLabel.setPixmap(pixmap)

        print(self.ImageLabel.size())
        print(self.ImageLabel.size().width())
        print(type(self.ImageLabel.size().width()))


    def ImageSelectorBind(self):
        self.NextImageButton.clicked.connect(
            lambda: self.display_image(is_next=1))
        self.LastImageButton.clicked.connect(
            lambda: self.display_image(is_next=-1))
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        # return super().resizeEvent(event)
        # 当窗口大小改变时，此方法会被调用
        # event.size() 包含了新的窗口大小
        self.display_image(is_next=0)
        


def ui_run():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    ui_run()
