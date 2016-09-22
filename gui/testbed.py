import sys
import math
from OpenGL.GL import *
from PySide import QtCore, QtGui, QtOpenGL


class LocalWidget(QtOpenGL.QGLWidget):
    zRotationChanged = QtCore.Signal(int)

    def __init__(self, controls, parent=None):
        super(LocalWidget, self).__init__(parent)
        self.width = 0
        self.height = 0
        # self._bubble = Bubble(- 3.0, 1.0, 1.0)
        self._controls = controls
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateGL)
        timer.start(40)

    def render(self):
        for a in self._controls:
            a.render()

    def __del__(self):
        print "GLWidget.__del__"
        self.makeCurrent()

    def initializeGL(self):
        print "GLWidget.initializeGL"

        # glEnable(GL_BLEND)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0, 0.0, 0.0, 0.0)
        glPushMatrix()
        self.render()
        glPopMatrix()

    def resizeGL(self, width, height):
        print "GLWidget.resizeGL"

        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, +1.0, -1.0, 1.0, 5.0, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0, -40.0)

    def mousePressEvent(self, event):
        print "dx %d" % event.x()
        print "dy %d" % event.y()

    def mouseMoveEvent(self, event):
        print "dx %d" % event.x()
        print "dy %d" % event.y()


class MainWindow(QtGui.QMainWindow):
    def __init__(self, controls):
        print "DisplayEngine.__init__"
        super(MainWindow, self).__init__()
        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)
        self.glWidget = LocalWidget(controls)

        self.glWidgetArea = QtGui.QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QtGui.QSizePolicy.Ignored,
                                        QtGui.QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)
        central_layout = QtGui.QGridLayout()
        central_layout.addWidget(self.glWidgetArea, 0, 0, 4, 4)
        central_widget.setLayout(central_layout)
        self.setWindowTitle("Visual Log Monitor")
        self.resize(600, 600)
