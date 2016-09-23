class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Bounds(object):
    def __init__(self, left=0, right=0, top=0, bottom=0):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


class Control(object):
    def __init__(self):
        pass

    def render(self, bounds):
        pass
