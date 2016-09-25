import sys
import control

from PySide import QtGui

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class ALine(control.Control):
    def __init__(self):
        """

        """
        super(control.Control, self).__init__()
        self._controls = {}

    def render(self):
        """

        :return:
        """
        self.draw_line()
        for key, value in self._controls.items():
            value.render()
        return True

    def add(self, pos, c):
        """

        :param pos:
        :param c:
        :return:
        """
        self._controls[pos] = c

    def draw_line(self):
        """

        :return:
        """
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        glVertex2f(self.bounds.left_top.x, self.bounds.left_top.y)
        glVertex2f(self.bounds.right_bottom.x, self.bounds.right_bottom.y)
        glEnd()


if __name__ == '__main__':
    list = []

    app = QtGui.QApplication(sys.argv)
    import start
    import circle

    for i in range(-5, 8):
        bounds = control.Bounds(control.Point(-7.9, i), control.Point(8, i))
        lineA = ALine()
        lineA.set_bounds(bounds)
        list.append(lineA)
        s = start.StartControl()
        c = circle.Circle()
        sbounds = control.Bounds(control.Point(-7.9, i - 0.2), control.Point(-6.9, i + 0.2))
        sbounds.print_me()
        c.set_bounds(sbounds)

        s.set_bounds(sbounds)
        list.append(c)
        list.append(s)


    import testbed

    mainWin = testbed.MainWindow(list)
    mainWin.show()
    sys.exit(app.exec_())
