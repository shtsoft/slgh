#!/usr/bin/env python3


import unittest


from slgh.lib import LibClass
from slgh.lib import _private_lib_function
from slgh.lib import lib_function


class TestLib(unittest.TestCase):

    def test_lib_class_method(self):
        self.assertEqual(LibClass.method(), 0)

    def test__private_lib_function(self):
        self.assertEqual(_private_lib_function(), 0)

    def test_lib_function(self):
        self.assertEqual(lib_function(), 0)


if __name__ == '__main__':
    unittest.main()
