import unittest
import os
from geodist import *

class TestModuleDistanceBetween(unittest.TestCase):

    def test_coords(self):
        """Test to make sure distance from geodist module between 2 co-ords is within 0.1 a km of the value from https://gps-coordinates.org/distance-between-coordinates.php"""

        latlngA = {50.71527036, -2.44427954}
        latlngB = {50.71520046, -2.44137513}
        expectedOutput = 0.20
        actualOutput = distance(latlngA, latlngB)
        
        self.assertTrue(actualOutput < expectedOutput +0.1 and actualOutput > expectedOutput -0.1)
    
    def test_west_east_coord(self):
        """Test to make sure co-ds furthest West and East in Devon and Cornwall return expected value within 0.1km"""

        latlngA = {50.793569, -2.887478} # East Devon
        latlngB = {50.065787, -5.712524} # West Cornwall
        expectedOutput = 215.84
        actualOutput = distance(latlngA, latlngB)
        
        self.assertTrue(actualOutput < expectedOutput +0.1 and actualOutput > expectedOutput -0.1)
        
    def test_north_south_cord(self):
        """TTest to make sure co-ds furthest North and South in Devon and Cornwall return expected value within 0.1km"""

        latlngA = [51.245284, -3.785560] # North Devon
        latlngB = {49.959701, -5.206656} # South Conwall
        expectedOutput = 174.62
        actualOutput = distance(latlngA, latlngB)
        
        self.assertTrue(actualOutput < expectedOutput +0.1 and actualOutput > expectedOutput -0.1)
    
    def test_empty_coords(self):
        """Test to make sure 2 empty co-ords returns -1"""

        latlngA = {}
        latlngB = {}
        expectedOutput = -1
        actualOutput = distance(latlngA, latlngB)
        
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_empty_lat(self):
        """Test to make sure empty lat co-ords returns -1"""

        latlngA = {50.71527036}
        latlngB = {50.71527046}
        expectedOutput = -1
        actualOutput = distance(latlngA, latlngB)
        
        self.assertEqual(actualOutput, expectedOutput)
        

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
