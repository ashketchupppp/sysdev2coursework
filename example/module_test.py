import unittest
from module import *

# you run this file just like any other python file to run the tests

# we are testings the function pow not only returns the correct
# value but also that it responds in the way we want when given something odd
# e.g. the letter a

# each test should aim to test only ONE thing e.g. on function.
# ideally you should have multiple test cases for a single function
# to prove that it is thoroughly tested.
# i would recommend that you have one test class for each thing you are testing.

# naming convention of the test suite could be "Test<ModuleName><TestedFunctionalityName>"
class TestModulePow(unittest.TestCase):

    # tests always have the prefix "test_"
    def test_valid_pow(self):
        # put docstrings in, good practice and you get marked down if you dont :(
        """Test a valid number."""
        self.assertEqual(25, pow(5, 2))

    def test_string_pow_base(self):
        """Test to make sure that pow throws an exception when passed a string as the base."""
        with self.assertRaises(TypeError):
            pow('a', 2)

    def test_string_pow_exponent(self):
        """Test to make sure that pow throws an exception when passed a string as the exponent."""
        with self.assertRaises(TypeError):
            pow(5, 'a')

class TestModuleAdd(unittest.TestCase):

    def test_valid_add(self):
        """Test adding two positive numbers."""
        self.assertEqual(5, add(2, 3))

    def test_valid_add_one_negative(self):
        """Test adding a negative and a positive number."""
        self.assertEqual(1, add(4, -3))

    def test_valid_add_two_negative(self):
        """Test adding a negative and a positive number."""
        self.assertEqual(-5, add(-2, -3))

    def test_invalid_add(self):
        """Test adding a string to a number."""
        with self.assertRaises(TypeError):
            add('a', 3)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
