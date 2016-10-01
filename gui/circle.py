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


import math
from OpenGL.GL import *
import control
import dot
import sys
from PySide import QtGui


class Circle(control.Control):
    def __init__(self,center=0, radius=0):
        super(control.Control, self).__init__()
        self._controls = {}
        self._dot = dot.Dot()
        self._num_triangles = 100
        self.center = center
        self.radius = radius

    def render(self):
        if self.center is 0:
            self.bounds.left_top.x += 0.1
            self.bounds.right_bottom.x += 0.1
            self.center = self.bounds.center()
            self.radius = self.bounds.width()/2

        self.draw_circle(self.center.x, self.center.y, self.radius)
        self._dot.set_bounds(control.Bounds(self.center, self.center))
        self._dot.render()

        for key, value in self._controls.items():
            value.render()
        return True

    def add(self, pos, c):
        self._controls[pos] = c

    def draw_circle(self, x, y, w):
        # print "draw_circle x=%d y=%d w=%d" % (x, y, w)

        self._num_triangles -= 10
        if self._num_triangles == 0:
            self._num_triangles = 100

        twice_the_pi = 3.14159 * 2
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        for i in range(self._num_triangles + 1):
            glVertex2f(x + (w * math.cos(i * twice_the_pi / self._num_triangles)),
                       y + (w * math.sin(i * twice_the_pi / self._num_triangles)))
        glEnd()

if __name__ == '__main__':
    list = []

    app = QtGui.QApplication(sys.argv)
    bound = control.Bounds(control.Point(-7.0, 1.0), control.Point(-5.0, 3.0))
    circle = Circle()
    circle.set_bounds(bound)

    list.append(circle)

    import testbed

    mainWin = testbed.MainWindow(list)
    mainWin.show()
    sys.exit(app.exec_())

