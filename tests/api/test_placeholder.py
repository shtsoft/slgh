import unittest


from slgh.api.placeholder import placeholder_function
from slgh.api.placeholder import PlaceholderClass


class TestLib(unittest.TestCase):

    def test_lib_function(self):
        self.assertEqual(placeholder_function(0, 0), 0)

    def test_lib_class_method(self):
        placeholder_object = PlaceholderClass(0)
        self.assertEqual(placeholder_object.method(), 0)


if __name__ == '__main__':
    unittest.main()
