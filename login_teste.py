# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'login_teste.ui'
##
# Created by: Qt User Interface Compiler version 5.15.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 700)
        MainWindow.setMinimumSize(QSize(500, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 40))
        self.top_bar.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.frame_error = QFrame(self.top_bar)
        self.frame_error.setObjectName(u"frame_error")
        self.frame_error.setMaximumSize(QSize(450, 16777215))
        self.frame_error.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
                                       "border-radius: 10px ")
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.label_error = QLabel(self.frame_error)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton = QPushButton(self.frame_error)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(20, 20))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
                                      "	border-radius: 5px\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	color: rgb(200, 200, 200);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "	color: rgb(200, 200, 200);\n"
                                      "	background-color: rgb(80, 80, 80);\n"
                                      "}")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalLayout_2.addWidget(self.frame_error)

        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(152, 152, 152);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_area = QFrame(self.content)
        self.login_area.setObjectName(u"login_area")
        self.login_area.setMaximumSize(QSize(450, 550))
        self.login_area.setStyleSheet(u"background-color: rgb(89, 89, 89);")
        self.login_area.setFrameShape(QFrame.NoFrame)
        self.login_area.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.login_area)

        self.verticalLayout.addWidget(self.content)

        self.bottom = QFrame(self.centralwidget)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMaximumSize(QSize(16777215, 40))
        self.bottom.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 903, 20))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_error.setText(QCoreApplication.translate(
            "MainWindow", u"TextLabel", None))
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", u"X", None))
    # retranslateUi
