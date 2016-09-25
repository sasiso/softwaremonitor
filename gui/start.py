from OpenGL.GL import *
import control


class StartControl(control.Control):
    def __init__(self):
        super(control.Control, self).__init__()

    def render(self):
        self.bounds.left_top.x += 0.05
        self.bounds.right_bottom.x += 0.05

        x1 = self.bounds.left_top.x
        x2 = self.bounds.left_top.x
        x3 = self.bounds.right_bottom.x
        y1 = self.bounds.left_top.y
        y2 = self.bounds.right_bottom.y
        y3 = self.bounds.right_bottom.y - self.bounds.height()/2.0

        glBegin(GL_TRIANGLES)
        glColor3f(0, 1, 0)

        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x3, y3, 0)
        glEnd()
        return True
