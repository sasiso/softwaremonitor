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
