import sys

from PySide import QtGui

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class ALine:
    def __init__(self, x1, y1, x2, y2, width):
        print "ALine.__init__"
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = width
        self._controls = {}

    def render(self):
        self.draw_line()
        for key, value in self._controls.items():
            value.render()

    def add(self, pos, control):
        self._controls[pos] = control

    def draw_line(self):
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glEnd()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    line = ALine(-7.9, 1, 7.9, 1, .03)
    import testbed

    mainWin = testbed.MainWindow(line)
    mainWin.show()
    sys.exit(app.exec_())
