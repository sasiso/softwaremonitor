import sys
import math
from PySide import QtGui
import dot

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class Circle:
    def __init__(self, x1, y1, w):
        print "ALine.__init__"
        self._x = x1
        self._y = y1
        self._w = w
        self._controls = {}
        self._dot = dot.Dot(self._x, self._y, 0)
        self._num_triangles = 100

    def render(self):
        self.draw_circle()
        self._dot.render()
        for key, value in self._controls.items():
            value.render()

    def add(self, pos, control):
        self._controls[pos] = control

    def draw_circle(self):
        self._num_triangles -= 10
        if self._num_triangles == 0:
            self._num_triangles = 100

        twice_the_pi = 3.14159 * 2
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        for i in range(self._num_triangles + 1):
            glVertex2f(self._x + (self._w * math.cos(i * twice_the_pi / self._num_triangles)),
                       self._y + (self._w * math.sin(i * twice_the_pi / self._num_triangles)))
        glEnd()


if __name__ == '__main__':
    list = []

    app = QtGui.QApplication(sys.argv)
    circle = Circle(-1.9, 1, 1)

    list.append(circle)

    import testbed

    mainWin = testbed.MainWindow(list)
    mainWin.show()
    sys.exit(app.exec_())
