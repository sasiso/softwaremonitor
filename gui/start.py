import sys
import control

from OpenGL.GL import *
from PySide import QtCore, QtGui, QtOpenGL
import control


class StartControl(control.Control):
    def __init__(self, x, y, w):
        super(control.Control, self).__init__()
        self._x = x
        self._y = y
        self._w = w
        pass

    def render(self, bounds):
        self._x += 0.01
        if self._x == 5:
            self._x = -3.0
        x1 = self._x
        x2 = self._x
        x3 = self._x + self._w / 2
        y1 = self._y + self._w / 2
        y2 = self._y - self._w / 2
        y3 = self._y

        glBegin(GL_TRIANGLES)
        glColor3f(0, 1, 0)

        glVertex3f(x1, y1, 0)
        glVertex3f(x2, y2, 0)
        glVertex3f(x3, y3, 0)
        glEnd()


class LocalWidget(QtOpenGL.QGLWidget):
    zRotationChanged = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(LocalWidget, self).__init__(parent)
        self.width = 0
        self.height = 0
        self._startControl = StartControl(- 3.0, 1.0, 1.0)
        self._bounds = control.Bounds()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.updateGL)
        timer.start(20)

    def render(self):
        self._startControl.render()

    def __del__(self):
        print "GLWidget.__del__"
        self.makeCurrent()

    def initializeGL(self):
        print "GLWidget.initializeGL"

        glEnable(GL_BLEND)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        self._startControl.render(self._bounds)
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
    def __init__(self):
        print "DisplayEngine.__init__"
        super(DisplayEngine, self).__init__()
        central_widget = QtGui.QWidget()
        self.setCentralWidget(central_widget)
        self.glWidget = LocalWidget()

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
        self.resize(800, 600)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = DisplayEngine()
    mainWin.show()
    sys.exit(app.exec_())
