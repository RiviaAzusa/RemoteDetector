import sys
from pathlib import Path
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QMainWindow, QPushButton,
                             QTextEdit, QGridLayout, QApplication, 
                             QToolButton, QDialog, QGraphicsView, QGraphicsScene,
                             QFrame)
from PyQt6.QtGui import QPixmap, QIcon,QColor
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem

from os import path
from random import randint

RESCOURCES_PATH = 'resources/'


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.show_square()
        # self.initUI()

    def initUI(self):
        self.square1 = QFrame(self)
        self.square1.setGeometry(150,20,100,100)
        self.square1.setStyleSheet("QWidget { background-color: %s }" %self.gen_color())

        self.square2 = QFrame(self)
        self.square2.setGeometry(150,20,100,100)
        self.square2.setStyleSheet("QWidget { background-color: %s }" %self.gen_color())
        

        grid = QGridLayout()
        # grid.setSpacing(10)
        grid.addWidget(self.square1, 0, 0)
        grid.addWidget(self.square2, 0, 1)


        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def show_square(self,):
            # 创建一个 QGraphicsView 和 QGraphicsScene
        view = QGraphicsView(self)
        scene = QGraphicsScene(self)
        view.setScene(scene)
        
        # 创建一个红色的正方形
        square = QGraphicsRectItem(0, 0, 100, 100)
        square.setBrush(QColor(255, 0, 0))  # 设置填充颜色为红色
        scene.addItem(square)
        
        # 调整视图的显示区域
        view.setSceneRect(square.rect())
        
        view.show()
    def gen_color(self):

        return QColor(randint(0,255),randint(0,255),randint(0,255))



class ImagesDisplayer(QWidget):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle('Image Displayer')
        self.resize(300, 300)
        self.initUI()

    def initUI(self,):
        self.image_displayer = QGraphicsView(self)
        self.image_displayer.setGeometry(20, 20, 260, 200)
        imgs = self.get_images(path.join(RESCOURCES_PATH, 'images'))
        img = QPixmap(imgs[0])
        img_scene = QGraphicsScene()
        img_scene.setSceneRect(0, 0, 300, 400)
        img_scene.addPixmap(img)
        self.change_imgs()
        self.image_displayer.setScene(img_scene)
        self.show()

    def get_images(self, path):
        supported_suffix = ['.jpg', '.png', 'jpeg']
        image_path = Path(path)
        image_files = [str(i) for i in image_path.iterdir()
                       if i.suffix in supported_suffix]
        return image_files

    def change_imgs(self):
        self.next_pic_button = QPushButton()
        self.next_pic_button.setIcon(
            QIcon(path.join(RESCOURCES_PATH, 'icons', 'right.svg')))
        self.show()


def main():

    app = QApplication(sys.argv)
    # a = ImagesDisplayer()
    a = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
