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


class Fse(control.Control):

    def __init__(self, bounds=None):
        super(control.Control, self).__init__()
        if bounds is not None:
            self.bounds = bounds

    def render(self):
        glBegin(GL_TRIANGLES)
        glColor3f(0, 1, 0)
        glEnd()
        return True
