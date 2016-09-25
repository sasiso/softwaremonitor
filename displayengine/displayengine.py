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
        engine = userinterface.UserInterface(channel)
        engine.show()
        sys.exit(app.exec_())

    def register(self, source):
        return self.source_mgr.register_source(source)
