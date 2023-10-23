# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoteDetector.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)
from resources import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 678)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(830, 640))
        self.MainWidget = QWidget(MainWindow)
        self.MainWidget.setObjectName(u"MainWidget")
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setMinimumSize(QSize(830, 600))
        self.horizontalLayout_3 = QHBoxLayout(self.MainWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.MainBox = QGroupBox(self.MainWidget)
        self.MainBox.setObjectName(u"MainBox")
        sizePolicy.setHeightForWidth(self.MainBox.sizePolicy().hasHeightForWidth())
        self.MainBox.setSizePolicy(sizePolicy)
        self.MainBox.setMinimumSize(QSize(830, 600))
        self.MainBox.setMaximumSize(QSize(3840, 2160))
        self.MainBox.setFlat(True)
        self.MainBox.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.MainBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MainHLayout = QHBoxLayout()
        self.MainHLayout.setObjectName(u"MainHLayout")
        self.LeftVLayout = QVBoxLayout()
        self.LeftVLayout.setObjectName(u"LeftVLayout")
        self.LeftVLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.LeftSubVLayout = QVBoxLayout()
        self.LeftSubVLayout.setObjectName(u"LeftSubVLayout")
        self.LeftSubVLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.ImageLabel = QLabel(self.MainBox)
        self.ImageLabel.setObjectName(u"ImageLabel")
        self.ImageLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMinimumSize(QSize(640, 450))

        self.LeftSubVLayout.addWidget(self.ImageLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.LastImageButton = QPushButton(self.MainBox)
        self.LastImageButton.setObjectName(u"LastImageButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LastImageButton.sizePolicy().hasHeightForWidth())
        self.LastImageButton.setSizePolicy(sizePolicy1)
        self.LastImageButton.setMinimumSize(QSize(0, 50))
        self.LastImageButton.setMaximumSize(QSize(150, 50))
        icon = QIcon()
        icon.addFile(u":/icons/left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LastImageButton.setIcon(icon)
        self.LastImageButton.setIconSize(QSize(32, 32))
        self.LastImageButton.setFlat(False)

        self.horizontalLayout.addWidget(self.LastImageButton)

        self.NextImageButton = QPushButton(self.MainBox)
        self.NextImageButton.setObjectName(u"NextImageButton")
        sizePolicy1.setHeightForWidth(self.NextImageButton.sizePolicy().hasHeightForWidth())
        self.NextImageButton.setSizePolicy(sizePolicy1)
        self.NextImageButton.setMinimumSize(QSize(150, 50))
        self.NextImageButton.setMaximumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NextImageButton.setIcon(icon1)
        self.NextImageButton.setIconSize(QSize(32, 32))
        self.NextImageButton.setFlat(False)

        self.horizontalLayout.addWidget(self.NextImageButton)


        self.LeftSubVLayout.addLayout(self.horizontalLayout)


        self.LeftVLayout.addLayout(self.LeftSubVLayout)


        self.MainHLayout.addLayout(self.LeftVLayout)

        self.RightVLayout = QVBoxLayout()
        self.RightVLayout.setObjectName(u"RightVLayout")
        self.RightVLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.RightSubHLayout = QVBoxLayout()
        self.RightSubHLayout.setObjectName(u"RightSubHLayout")
        self.RightSubHLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.ModelSelectionButton = QPushButton(self.MainBox)
        self.ModelSelectionButton.setObjectName(u"ModelSelectionButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/wrench.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ModelSelectionButton.setIcon(icon2)

        self.RightSubHLayout.addWidget(self.ModelSelectionButton)

        self.ModelSettingButton = QPushButton(self.MainBox)
        self.ModelSettingButton.setObjectName(u"ModelSettingButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/setting.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ModelSettingButton.setIcon(icon3)

        self.RightSubHLayout.addWidget(self.ModelSettingButton)

        self.InputSelectionButton = QPushButton(self.MainBox)
        self.InputSelectionButton.setObjectName(u"InputSelectionButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/selection.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.InputSelectionButton.setIcon(icon4)

        self.RightSubHLayout.addWidget(self.InputSelectionButton)

        self.LogDisplayer = QTextBrowser(self.MainBox)
        self.LogDisplayer.setObjectName(u"LogDisplayer")

        self.RightSubHLayout.addWidget(self.LogDisplayer)


        self.RightVLayout.addLayout(self.RightSubHLayout)


        self.MainHLayout.addLayout(self.RightVLayout)

        self.MainHLayout.setStretch(0, 4)
        self.MainHLayout.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.MainHLayout)


        self.horizontalLayout_3.addWidget(self.MainBox)

        MainWindow.setCentralWidget(self.MainWidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 883, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.LastImageButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainBox.setTitle("")
        self.ImageLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LastImageButton.setText(QCoreApplication.translate("MainWindow", u"Last Image", None))
        self.NextImageButton.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.ModelSelectionButton.setText(QCoreApplication.translate("MainWindow", u"Model Selection", None))
        self.ModelSettingButton.setText(QCoreApplication.translate("MainWindow", u"Model Setting", None))
        self.InputSelectionButton.setText(QCoreApplication.translate("MainWindow", u"Input Selection", None))
    # retranslateUi

