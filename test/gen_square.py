import sys
from PyQt6.QtWidgets import QApplication, QGraphicsView
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGraphicsScene, QGraphicsRectItem

def main():
    app = QApplication(sys.argv)
    
    # 创建一个 QGraphicsView 和 QGraphicsScene
    view = QGraphicsView()
    scene = QGraphicsScene()
    view.setScene(scene)
    
    # 创建一个红色的正方形
    square = QGraphicsRectItem(0, 0, 100, 100)
    square.setBrush(QColor(255, 0, 0))  # 设置填充颜色为红色
    scene.addItem(square)
    
    # 调整视图的显示区域
    view.setSceneRect(square.rect())
    
    view.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
