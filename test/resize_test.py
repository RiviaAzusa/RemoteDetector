import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)  # 设置窗口的初始位置和大小
        self.setWindowTitle('窗口大小改变事件监测示例')
        
    def resizeEvent(self, event):
        # 当窗口大小改变时，此方法会被调用
        # event.size() 包含了新的窗口大小
        new_size = event.size()
        print(f'窗口大小改变为：{new_size.width()} x {new_size.height()}')

def main():
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
