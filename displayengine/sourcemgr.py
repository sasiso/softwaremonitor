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
from gui import control
from gui import circle
from gui import line
from gui import textdraw

from PySide import QtCore

LEFT = -7.9
RIGHT = -6.9
TOP = -7
BOTTOM = 8

LEN = 15

Gap = 2.0


class SourceManager(object):
    """

    """

    def __init__(self):
        """

        """
        self.sources = {}
        self._index = 0
        pass

    def register_source(self, source):
        """ Register an source with manager

        :param source: input source
        :return: index number of this source, this index can be later used to delete this source
        """
        self._index += 1
        self.sources[self._index] = source

        return self._index

    def delete_source(self, index):
        del self.sources[index]

    def getControls(self):
        """

        :return:
        """
        controls = []
        text = []
        data = self.sources[1].get_data()
        y_axis = 0
        for key, value in data.iteritems():
            y_axis += 1
            t = textdraw.Text()
            t.x = LEFT
            t.y = y_axis + 0.2
            t.text = key
            text.append(t)
            bounds = control.Bounds(control.Point(LEFT, y_axis), control.Point(BOTTOM, y_axis))
            lineA = line.ALine()
            lineA.set_bounds(bounds)
            controls.append(lineA)
            for a in value:
                x_axis = LEFT + (self.sources[1].getpos(a) * LEN)
                c = circle.Circle()
                sbounds = control.Bounds(control.Point(x_axis - 0.5, y_axis - 0.5),
                                         control.Point(x_axis + 0.5, y_axis + 0.5))
                c.set_bounds(sbounds)
                controls.append(c)
                pass

        return controls, text
