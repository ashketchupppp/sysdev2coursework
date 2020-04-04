"""NOT COMPLETE - GET ERROR SAYING MODULE UI CANNOT BE FOUND"""

import unittest
import os
from filter import *

class TestFilter(unittest.TestCase):
    def test_valid_entry(self):
        """Test if expected result is returned with valid list."""
        postcodelatlong = ["50.7371664", "-3.53592217"]
        crimedata = [
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""},
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""},
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""},
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""},
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""},
            {"Crime type": "Anti-social behaviour", "Latitude": "", "Longitude": ""}
            ]
        actualOutput = filterData(crimedata, postcodelatlong, radius)
        expectedOutput = ["+50.71167397", "-2.43695132"]
        self.assertEqual(actualOutput, expectedOutput)
        
    

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()