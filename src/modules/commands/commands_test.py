import unittest
import os
from commands import *

class TestCommandPostcodeFcuntion(unittest.TestCase):
    def test_valid_entry(self):
        """Test if expeted result is retuned with valid list."""
        postcode = "TQ1 3QU"
        actualOutput = find_postcode_coordinate(postcodes)
        expectedOutput = "Lattitude: +50.47696028Longitude: -3.51907083"
        self.assertEqual(actualOutput, expectedOutput)
        
if __name__ == '__main__':
    unittest.main()