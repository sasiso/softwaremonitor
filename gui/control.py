class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y


class Bounds(object):
    left_top = Point()
    right_bottom = Point()

    def __init__(self, lefttop=Point(), rightbottom=Point()):
        self.left_top = lefttop
        self.right_bottom = rightbottom

    def center(self):
        return Point((self.left_top.x+ self.right_bottom.x)/2.0,
                     (self.right_bottom.y + self.left_top.y)/2.0)

    def width(self):
        return abs(self.left_top.x - self.right_bottom.x)

    def height(self):
        return abs(self.left_top.y - self.right_bottom.y)

    def print_me(self):
        print "top x=%d y=%d, bottom x=%d y=%d" % (self.left_top.x, self.left_top.y, self.right_bottom.x, self.right_bottom.y)


class Control(object):
    bounds = Bounds()

    def __init__(self):
        self.bounds = Bounds()

    def set_bounds(self, bounds):
        import copy
        self.bounds = copy.deepcopy(bounds)

    def get_bounds(self):
        return self.bounds

    def render(self, bounds):
        pass
