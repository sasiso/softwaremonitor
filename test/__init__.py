import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print "In setup"
        pass

    def tearDown(self):
        print "In teardown"

    def test(self, type_name):
        b = type_name()
        return b.render()

    def test_all_control(self):
        from gui import balloon
        self.assertTrue(self.test(balloon.Balloon))

        from gui import bubble
        self.assertTrue(self.test(bubble.Bubble))

        from gui import circle
        self.assertTrue(self.test(circle.Circle))

        from gui import dot
        self.assertTrue(self.test(dot.Dot))

        from gui import error
        self.assertTrue(self.test(error.Error))

        from gui import exception
        self.assertTrue(self.test(exception.Exception))

        from gui import fse
        self.assertTrue(self.test(fse.Fse))

        from gui import line
        self.assertTrue(self.test(line.Line))

        from gui import start
        self.assertTrue(self.test(start.Start))

        from gui import user
        self.assertTrue(self.test(user.User))



if __name__ == '__main__':
    unittest.main()
