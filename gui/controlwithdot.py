import control
import dot


class ControlWithDot(control):

    def __init__(self):
        super(control.Control, self).__init__()
        self._dot = dot.Dot()

    def render(self, bounds):
        pass