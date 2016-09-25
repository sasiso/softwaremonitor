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
import math
from OpenGL.GL import *
import control


class Bubble(control.Control):
    def __init__(self):
        super(control.Control, self).__init__()

    def render(self):
        # todo read from bounds
        x = self.bounds.left_top.x
        y = self.bounds.left_top.y
        w = self.bounds.width()

        num_triangles = 20
        twice_the_pi = 3.14159 * 2
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 1, 0)
        glVertex2f(x, y)
        for i in range(num_triangles + 1):
            glVertex2f(x + (w * math.cos(i * twice_the_pi / num_triangles)),
                       y + (w * math.sin(i * twice_the_pi / num_triangles)))
        glEnd()
        return True
