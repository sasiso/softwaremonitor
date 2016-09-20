from PySide import QtCore, QtGui
import ui_mainwindow


class MainWindow(QtGui.QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.show()