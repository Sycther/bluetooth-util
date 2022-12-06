# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(948, 616)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setGeometry(QRect(9, -1, 931, 561))
        sizePolicy.setHeightForWidth(self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.scanBtn = QPushButton(self.horizontalWidget)
        self.scanBtn.setObjectName(u"scanBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scanBtn.sizePolicy().hasHeightForWidth())
        self.scanBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.scanBtn)

        self.list = QListWidget(self.horizontalWidget)
        self.list.setObjectName(u"list")
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.list)

        self.saveBtn = QPushButton(self.horizontalWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy1.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.saveBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 948, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.scanBtn.clicked.connect(MainWindow.scanNow)
        self.saveBtn.clicked.connect(MainWindow.saveNow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.scanBtn.setText(QCoreApplication.translate("MainWindow", u"Scan BLE Devices", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save Output", None))
    # retranslateUi

