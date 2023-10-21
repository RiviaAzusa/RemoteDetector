
from PyQt6 import QtWidgets, QtGui
import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
Form.setWindowTitle('千牛编程思维')
Form.resize(300, 300)
grview = QtWidgets.QGraphicsView(Form)  # 加入 QGraphicsView
grview.setGeometry(20, 20, 260, 200)    # 设定 QGraphicsView 位置与大小
scene = QtWidgets.QGraphicsScene()      # 加入 QGraphicsScene
scene.setSceneRect(0, 0, 300, 400)      # 设定 QGraphicsScene 位置与大小
img = QtGui.QPixmap('pyqt_learn/imgs/test.png')         # 加入图片
scene.addPixmap(img)                    # 將图片加入 scene
grview.setScene(scene)                  # 设定 QGraphicsView 的场景為 scene
Form.show()
sys.exit(app.exec())