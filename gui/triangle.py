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
from OpenGL.GL import *
import control


class Triangle(object, control.Control):
    def __init__(self, center_x, center_y, width):
        self.centerX = center_x
        self.centerY = center_y
        self.width = width

    def render(self):
        glBegin(GL_TRIANGLES)
        self.centerX += 1.0
        x1 = self.centerX
        x2 = self.centerX - self.width / 2
        x3 = self.centerX + self.width / 2
        y1 = self.centerY + self.width / 2
        y2 = self.centerY - self.width / 2
        y3 = self.centerY - self.width / 2

        glColor3f(100, 122, 0.3)

        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x3, y3, 0)
        glEnd()
