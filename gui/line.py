"""
Copyright [2016] [Satbir Singh]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

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
        self._r = 0
        self._g = 1
        self._b = 0
        self._isStipple = False

    def enableStipple(self, flag):
        self._isStipple = flag

    def set_color(self, r=0, g=0, b=0):
        self._r = r
        self._g = g
        self._b = b

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
        if self._isStipple:
            glLineStipple(2, 0xAAAA)
            glEnable(GL_LINE_STIPPLE)

        glBegin(GL_LINES)
        glColor3f(self._r, self._g, self._b)
        glVertex2f(self.bounds.left_top.x, self.bounds.left_top.y)
        glVertex2f(self.bounds.right_bottom.x, self.bounds.right_bottom.y)
        glEnd()
        glDisable(GL_LINE_STIPPLE)


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
