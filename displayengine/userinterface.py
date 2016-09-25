#!/usr/bin/env python
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
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updateGL)

    def start(self, refresh_rate):
        self.timer.start(refresh_rate)

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


class UserInterface(QtGui.QMainWindow):
    def __init__(self, controls):
        super(UserInterface, self).__init__()
        self.refrsh_rate = 40

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
        self.exitAct = QtGui.QAction("E&xit", self, shortcut="Ctrl+Q",
                                     triggered=self.close)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.exitAct)

    def createSlider(self, changedSignal, setterSlot):
        slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QtGui.QSlider.TicksRight)

        slider.valueChanged.connect(setterSlot)
        changedSignal.connect(slider.setValue)
        return slider

    def start(self):
        self.glWidget.start(self.refrsh_rate)
