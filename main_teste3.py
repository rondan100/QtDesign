import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui
from teste3 import MyWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(320, 240)
    widget.show()

    sys.exit(app.exec_())
