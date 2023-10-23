# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smoke_detector.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QGridLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.LastImageButton = QPushButton(self.centralwidget)
        self.LastImageButton.setObjectName(u"LastImageButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.LastImageButton.sizePolicy().hasHeightForWidth())
        self.LastImageButton.setSizePolicy(sizePolicy)

        self.mainLayout.addWidget(self.LastImageButton, 13, 1, 1, 1)

        self.ModelSelector = QPushButton(self.centralwidget)
        self.ModelSelector.setObjectName(u"ModelSelector")

        self.mainLayout.addWidget(self.ModelSelector, 3, 2, 1, 1)

        self.ImageDisplayer = QLabel(self.centralwidget)
        self.ImageDisplayer.setObjectName(u"ImageDisplayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.ImageDisplayer.sizePolicy().hasHeightForWidth())
        self.ImageDisplayer.setSizePolicy(sizePolicy1)
        self.ImageDisplayer.setMaximumSize(QSize(3840, 2160))

        self.mainLayout.addWidget(self.ImageDisplayer, 1, 0, 12, 2)

        self.NextImageButton = QPushButton(self.centralwidget)
        self.NextImageButton.setObjectName(u"NextImageButton")

        self.mainLayout.addWidget(self.NextImageButton, 13, 0, 1, 1)

        self.ConnectionTest = QPushButton(self.centralwidget)
        self.ConnectionTest.setObjectName(u"ConnectionTest")

        self.mainLayout.addWidget(self.ConnectionTest, 1, 2, 1, 1)

        self.LogPrinter = QTextBrowser(self.centralwidget)
        self.LogPrinter.setObjectName(u"LogPrinter")

        self.mainLayout.addWidget(self.LogPrinter, 4, 2, 10, 1)

        self.ModelSetting = QPushButton(self.centralwidget)
        self.ModelSetting.setObjectName(u"ModelSetting")

        self.mainLayout.addWidget(self.ModelSetting, 2, 2, 1, 1)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 940, 24))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.LastImageButton.setText(QCoreApplication.translate("MainWindow", u"Last Image", None))
        self.ModelSelector.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.ImageDisplayer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.NextImageButton.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.ConnectionTest.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u6d4b\u8bd5", None))
        self.LogPrinter.setMarkdown(QCoreApplication.translate("MainWindow", u"## \u8fd9\u91cc\u663e\u793a\u4e00\u4e9b\u5b9e\u65f6log\n"
"\n"
"", None))
        self.ModelSetting.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

