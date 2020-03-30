import unittest
from filter import *

"""Here is an example dictionary, used to test the sort functions work correctly in the sort module"""
dicts = [
    {'first': 'Jim', 'distance': 2.8}, 
    {'first': 'James','distance': 7.5},
    {'first': 'Claire','distance': 1.3},
    {'first': 'Sam','distance': 0.1},
    {'first': 'Olivia','distance': 12.5},
    {'first': 'Christian','distance': 4.9}
    ]

class TestModuleFilter(unittest.TestCase):
    def test_filter_function(self):
        """ Checks sort function sorts alphabetically descending. """
        expectedOutput = [{'first': 'Jim', 'distance': 2.8}, {'first': 'Claire', 'distance': 1.3}, {'first': 'Sam', 'distance': 0.1}, {'first': 'Christian', 'distance': 4.9}]
        
    
        actualOutput = filterData(dicts, 'distance', 5)
        self.assertEqual(actualOutput, expectedOutput)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
