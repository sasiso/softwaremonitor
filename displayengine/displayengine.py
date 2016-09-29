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
from PySide import QtGui
from PySide import QtCore

import userinterface
import sourcemgr

LEFT = -7.9
RIGHT = -6.9
TOP = -7
BOTTOM = 8


class DisplayEngine(object):
    source_mgr = sourcemgr.SourceManager()

    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.ui = userinterface.UserInterface()
        self.ui.show()

        self.timer = QtCore.QTimer(self.ui.glWidget)
        self.timer.timeout.connect(self.update)
        self.timer.start(40)

    def update(self):
        c, t = self.source_mgr.getControls()
        self.ui.set_controls(c, t)
        self.ui.on_update()

    def register(self, source):
        return self.source_mgr.register_source(source)

    def set_refresh_rate(self, ms):
        self.ui.set_refresh_rate(ms)

    def start(self):
        sys.exit(self.app.exec_())
