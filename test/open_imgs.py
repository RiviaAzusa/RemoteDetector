import sys
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QWidget

class ImageLoaderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Loader")
        self.setGeometry(100, 100, 400, 300)

        # 创建布局和窗口主部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 创建加载图片按钮
        self.load_button = QPushButton("加载图片", self)
        self.load_button.clicked.connect(self.load_image)

        # 创建标签用于显示图片
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.load_button)
        layout.addWidget(self.image_label)

    def load_image(self):
        home_dir = str(Path.home())
        selected_files = QFileDialog.getOpenFileName(self, 'Open file', home_dir)
        file_path = selected_files[0]
        # 使用QPixmap加载图像并在标签上显示
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageLoaderApp()
    window.show()
    sys.exit(app.exec())
