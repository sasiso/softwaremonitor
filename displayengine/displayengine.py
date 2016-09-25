"""

"""
import sys
from PySide import QtGui

import userinterface
import sourcemgr


class DisplayEngine(object):
    source_mgr = sourcemgr.SourceManager()

    def __init__(self):
        app = QtGui.QApplication(sys.argv)
        channel = []
        self.ui = userinterface.UserInterface(channel)
        self.ui.show()
        sys.exit(app.exec_())

    def register(self, source):
        return self.source_mgr.register_source(source)

    def set_refresh_rate(self, ms):
        self.ui.set_refresh_rate(ms)

