#!/usr/bin/env python

import sys
from PySide import QtCore, QtGui, QtOpenGL

try:
    from OpenGL.GL import *
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL grabber",
                               "PyOpenGL must be installed to run this example.")
    sys.exit(1)


class GLWidget(QtOpenGL.QGLWidget):
    zRotationChanged = QtCore.Signal(int)

    def __init__(self, controls, parent=None):
        super(GLWidget, self).__init__(parent)
        self._controls = controls
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateGL)
        timer.start(20)

    def render(self):
        for a in self._controls:
            a.render()

    def __del__(self):
        print "GLWidget.__del__"
        self.makeCurrent()

    def on_slider(self, angle):
        print "GLWidget.on_slider"
        pass

    def initializeGL(self):
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


class DisplayEngine(QtGui.QMainWindow):
    def __init__(self, controls):
        print "DisplayEngine.__init__"
        super(DisplayEngine, self).__init__()

        centralWidget = QtGui.QWidget()
        self.setCentralWidget(centralWidget)

        self.glWidget = GLWidget(controls)
        self.pixmapLabel = QtGui.QLabel()

        self.glWidgetArea = QtGui.QScrollArea()
        self.glWidgetArea.setWidget(self.glWidget)
        self.glWidgetArea.setWidgetResizable(True)
        self.glWidgetArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.glWidgetArea.setSizePolicy(QtGui.QSizePolicy.Ignored,
                                        QtGui.QSizePolicy.Ignored)
        self.glWidgetArea.setMinimumSize(50, 50)

        self.pixmapLabelArea = QtGui.QScrollArea()
        self.pixmapLabelArea.setWidget(self.pixmapLabel)
        self.pixmapLabelArea.setSizePolicy(QtGui.QSizePolicy.Ignored,
                                           QtGui.QSizePolicy.Ignored)
        self.pixmapLabelArea.setMinimumSize(50, 50)

        zSlider = self.createSlider(self.glWidget.zRotationChanged,
                                    self.glWidget.on_slider)

        self.createActions()
        self.createMenus()

        centralLayout = QtGui.QGridLayout()
        centralLayout.addWidget(self.glWidgetArea, 0, 0, 4, 4)
        centralLayout.addWidget(self.pixmapLabelArea, 0, 10, 4, 1)

        centralLayout.addWidget(zSlider, 4, 0, 1, 4)
        centralWidget.setLayout(centralLayout)

        zSlider.setValue(0 * 16)

        self.setWindowTitle("Visual Log Monitor")
        self.resize(800, 600)

    def createActions(self):
        print "DisplayEngine.createActions"
        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                                     triggered=self.close)

    def createMenus(self):
        print "DisplayEngine.createMenus"
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAct)

    def createSlider(self, changedSignal, setterSlot):
        print "DisplayEngine.createSlider"
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QtGui.QSlider.TicksRight)

        slider.valueChanged.connect(setterSlot)
        changedSignal.connect(slider.setValue)
        return slider
