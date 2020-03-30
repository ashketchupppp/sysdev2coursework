import unittest
import sort

"""Here is an example dictionary, used to test the sort functions work correctly in the sort module"""
unsortedDict = [
    {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, 
    {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, 
    {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, 
    {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, 
    {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, 
    {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, 
    {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}
    ]

class TestModuleSorter(unittest.TestCase):
    def test_crime_category_sort(self):
        """Checks sort function accurately sorts alphabetically by Crime Category"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}]
        
        actualOutput = sort.sortDistCrime(unsortedDict, 'Crime Category', False)
        self.assertEqual(actualOutput, expectedOutput)

    def test_crime_category_sort_reverse(self):
        """Checks sort function accurately sorts reverse alphabetically by Crime Category"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}]
        
        actualOutput = sort.sortDistCrime(unsortedDict, 'Crime Category', True)
        self.assertEqual(actualOutput, expectedOutput)

    def test_distance_sort_nearest(self):
        """Checks sort function accurately sorts by distance from postcode, nearest first"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}]
        
        actualOutput = sort.sortDistCrime(unsortedDict, 'Distance (km)', False)
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_distance_sort_furthest(self):
        """Checks sort function accurately sorts by distance from postcode, farthest first"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}]
        
        actualOutput = sort.sortDistCrime(unsortedDict, 'Distance (km)', True)
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_date_sort_newest(self):
        """Checks sort function accurately sorts by date and time, most recent first"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}]
        
        actualOutput = sort.sortDate(unsortedDict, True)
        self.assertEqual(actualOutput, expectedOutput)
      
    def test_distance_sort_oldest(self):
        """Checks sort function accurately sorts by date and time, oldest first"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}, {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}]
        
        actualOutput = sort.sortDate(unsortedDict, False)
        self.assertEqual(actualOutput, expectedOutput)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()