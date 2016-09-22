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
    list = []

    app = QtGui.QApplication(sys.argv)
    lineA = ALine(-7.9, 1, 7.9, 1, .03)
    lineB = ALine(-7.9, 2, 7.9, 2, .03)
    lineC = ALine(-7.9, 3, 7.9, 3, .03)
    lineD = ALine(-7.9, 4, 7.9, 4, .03)
    lineE = ALine(-7.9, 5, 7.9, 5, .03)
    lineF = ALine(-7.9, 6, 7.9, 6, .03)
    list.append(lineA)
    list.append(lineB)
    list.append(lineC)
    list.append(lineD)
    list.append(lineE)
    list.append(lineF)


    import bubble
    import start

    for i in range(10):
        t = start.StartControl(-7.9 + i + 0.5, 1, 0.2)
        lineA.add(i, t)

    import bubble
    import start

    for i in range(10):
        b = bubble.Bubble(-7.9 + i, 2, 0.1)
        lineB.add(i, b)

    import testbed

    mainWin = testbed.MainWindow(list)
    mainWin.show()
    sys.exit(app.exec_())
