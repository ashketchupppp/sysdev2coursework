import unittest
import os

from commands import find_postcode_coordinate
from ui.cli import InteractiveCommandLine

postcodes = [
{'Postcode': 'DT1 1AA', 'ETRS89GD-Lat': '+50.71527036', 'ETRS89GD-Long': '-2.44427954'},
{'Postcode': 'DT1 1AD', 'ETRS89GD-Lat': '+50.71167397', 'ETRS89GD-Long': '-2.43695132'},
{'Postcode': 'DT1 1AE', 'ETRS89GD-Lat': '+50.71329261', 'ETRS89GD-Long': '-2.43936007'}]
class TestCommandPostcodeFcuntion(unittest.TestCase):
    def test_valid_entry(self):
        """Test if expeted result is retuned with valid list."""
        postcode = "DT1 1AD"
        actualOutput = find_postcode_coordinate(postcode, postcodes)
        expectedOutput = ["+50.71167397", "-2.43695132"]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_invalid_entry(self):
        """Test if False is returned is input is not a postcode."""
        postcode = "DT1 fds"
        actualOutput = find_postcode_coordinate(postcode, postcodes)
        expectedOutput = -1
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_empty_entry(self):
        """Test if False is returned if input is empty"""
        postcode = ""
        actualOutput = find_postcode_coordinate(postcode, postcodes)
        expectedOutput = -1
        self.assertEqual(actualOutput, expectedOutput)
        
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()