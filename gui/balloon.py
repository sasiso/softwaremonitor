from OpenGL.GL import *

import control


class Balloon(control.Control):

    def __init__(self):
        super(control.Control, self).__init__()

    def render(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0, 1, 0)
        glEnd()
        return True
