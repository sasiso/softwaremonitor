from OpenGL.GL import *

import control


class Explode(control.Control):

    def __init__(self, bounds=None):
        super(control.Control, self).__init__()
        if bounds is not None:
            self.bounds = bounds

    def render(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0, 1, 0)
        glEnd()
        return True

