import sys
import math
from OpenGL.GL import *
import control


class Bubble(object, control.Control):
    def __init__(self, x, y, w):
        self._x = x
        self._y = y
        self._w = w
        pass

    def render(self, bounds):
        num_triangles = 20
        twice_the_pi = 3.14159 * 2
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 1, 0)
        glVertex2f(self._x, self._y)
        for i in range(num_triangles + 1):
            glVertex2f(self._x + (self._w * math.cos(i * twice_the_pi / num_triangles)),
                       self._y + (self._w * math.sin(i * twice_the_pi / num_triangles)))
        glEnd()
