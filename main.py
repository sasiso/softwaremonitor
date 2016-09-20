import sys
import math
from PySide import QtCore, QtGui, QtOpenGL
from displayengine import displayengine

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    mainWin = displayengine.DisplayEngine()
    mainWin.show()
    sys.exit(app.exec_())
