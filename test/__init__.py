import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print "In setup"
        pass

    def tearDown(self):
        print "In teardown"

    @staticmethod
    def helper_test(type_name):
        b = type_name()
        return b.render()

    def test_all_control(self):
        from gui import balloon, circle, dot, bubble, error, exception, fse, line, start, user

        self.assertTrue(self.helper_test(balloon.Balloon))
        self.assertTrue(self.helper_test(bubble.Bubble))
        self.assertTrue(self.helper_test(circle.Circle))
        self.assertTrue(self.helper_test(dot.Dot))
        self.assertTrue(self.helper_test(error.Error))
        self.assertTrue(self.helper_test(exception.Exception))
        self.assertTrue(self.helper_test(fse.Fse))
        self.assertTrue(self.helper_test(line.ALine))
        self.assertTrue(self.helper_test(start.StartControl))
        self.assertTrue(self.helper_test(user.User))


if __name__ == '__main__':
    unittest.main()
