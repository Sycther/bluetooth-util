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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1258, 771)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 5, 1233, 701))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.list = QListWidget(self.gridLayoutWidget)
        self.list.setObjectName(u"list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy1)
        self.list.setMinimumSize(QSize(700, 0))

        self.gridLayout.addWidget(self.list, 3, 1, 2, 1)

        self.scanBtn = QPushButton(self.gridLayoutWidget)
        self.scanBtn.setObjectName(u"scanBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scanBtn.sizePolicy().hasHeightForWidth())
        self.scanBtn.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.scanBtn, 3, 0, 1, 1)

        self.saveBtn = QPushButton(self.gridLayoutWidget)
        self.saveBtn.setObjectName(u"saveBtn")
        sizePolicy1.setHeightForWidth(self.saveBtn.sizePolicy().hasHeightForWidth())
        self.saveBtn.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.saveBtn, 4, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(20)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.nameTxt = QLabel(self.gridLayoutWidget)
        self.nameTxt.setObjectName(u"nameTxt")
        font1 = QFont()
        font1.setPointSize(10)
        self.nameTxt.setFont(font1)
        self.nameTxt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameTxt)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.addrTxt = QLabel(self.gridLayoutWidget)
        self.addrTxt.setObjectName(u"addrTxt")
        self.addrTxt.setFont(font1)
        self.addrTxt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.addrTxt)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.detailsTxt = QLabel(self.gridLayoutWidget)
        self.detailsTxt.setObjectName(u"detailsTxt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.detailsTxt.sizePolicy().hasHeightForWidth())
        self.detailsTxt.setSizePolicy(sizePolicy4)
        self.detailsTxt.setFont(font1)
        self.detailsTxt.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.detailsTxt.setWordWrap(True)

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.detailsTxt)


        self.gridLayout.addLayout(self.formLayout, 3, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1258, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.scanBtn.clicked.connect(MainWindow.scanNow)
        self.saveBtn.clicked.connect(MainWindow.saveNow)
        self.list.itemActivated.connect(MainWindow.updateFormData)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.scanBtn.setText(QCoreApplication.translate("MainWindow", u"Scan BLE Devices", None))
        self.saveBtn.setText(QCoreApplication.translate("MainWindow", u"Save Output", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.nameTxt.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.addrTxt.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MetaData", None))
        self.detailsTxt.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

