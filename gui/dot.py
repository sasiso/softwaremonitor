import sys
import math
from PySide import QtGui

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class Dot:
    def __init__(self, x1, y1, w):
        print "ALine.__init__"
        self._x = x1
        self._y = y1
        self._w = w
        self._controls = {}

    def render(self):
        self.draw_dot()
        for key, value in self._controls.items():
            value.render()

    def draw_dot(self):
        glPointSize(2.0)
        glBegin(GL_POINTS)
        glColor3f(0.0, 0.0, 1.0)
        glVertex3f(self._x, self._y, 0.0)
        glEnd()

    def add(self, pos, control):
        self._controls[pos] = control


if __name__ == '__main__':
    list = []

    app = QtGui.QApplication(sys.argv)
    circle = Dot(-1.9, 1, 1)

    list.append(circle)

    import testbed

    mainWin = testbed.MainWindow(list)
    mainWin.show()
    sys.exit(app.exec_())
