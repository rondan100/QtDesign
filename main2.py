from teste2 import Ui_MainWindow
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class MainWindow(PySide2.QtWidgets.QMainWindow, Ui_MainWindow)


def __init__(self):
    super(MainWindow, self).__init__()
    self.setupUi(self)
