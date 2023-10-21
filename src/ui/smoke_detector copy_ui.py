# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smoke_detector copy.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ConnectionTest = QPushButton(self.centralwidget)
        self.ConnectionTest.setObjectName(u"ConnectionTest")
        self.ConnectionTest.setGeometry(QRect(640, 20, 151, 51))
        self.ModelSelector = QPushButton(self.centralwidget)
        self.ModelSelector.setObjectName(u"ModelSelector")
        self.ModelSelector.setGeometry(QRect(640, 110, 151, 51))
        self.ModelSetting = QPushButton(self.centralwidget)
        self.ModelSetting.setObjectName(u"ModelSetting")
        self.ModelSetting.setGeometry(QRect(640, 200, 151, 51))
        self.LogPrinter = QTextBrowser(self.centralwidget)
        self.LogPrinter.setObjectName(u"LogPrinter")
        self.LogPrinter.setGeometry(QRect(630, 270, 181, 81))
        self.ImageDisplayer = QLabel(self.centralwidget)
        self.ImageDisplayer.setObjectName(u"ImageDisplayer")
        self.ImageDisplayer.setGeometry(QRect(10, 10, 611, 481))
        self.LastImageButton = QPushButton(self.centralwidget)
        self.LastImageButton.setObjectName(u"LastImageButton")
        self.LastImageButton.setGeometry(QRect(650, 420, 100, 32))
        self.NextImageButton = QPushButton(self.centralwidget)
        self.NextImageButton.setObjectName(u"NextImageButton")
        self.NextImageButton.setGeometry(QRect(650, 470, 100, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 825, 24))
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
        self.ConnectionTest.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u6d4b\u8bd5", None))
        self.ModelSelector.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u9009\u62e9", None))
        self.ModelSetting.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bbe\u7f6e", None))
        self.LogPrinter.setMarkdown(QCoreApplication.translate("MainWindow", u"## \u8fd9\u91cc\u663e\u793a\u4e00\u4e9b\u5b9e\u65f6log\n"
"\n"
"", None))
        self.ImageDisplayer.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.LastImageButton.setText(QCoreApplication.translate("MainWindow", u"Last Image", None))
        self.NextImageButton.setText(QCoreApplication.translate("MainWindow", u"Next Image", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
    # retranslateUi

