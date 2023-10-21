import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage, QImageReader

class ImageDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Drop Widget')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.image_label)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        mime_data = event.mimeData()
        formats = QImageReader.supportedImageFormats()
        if mime_data.hasUrls() and any([url.toString().toLower() for url in mime_data.urls() if url.toLocalFile().toLower().endswith(format) for format in formats]):
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        image_path = mime_data.urls()[0].toLocalFile()

        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
            event.acceptProposedAction()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setCentralWidget(ImageDropWidget())

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
