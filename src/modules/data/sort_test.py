import unittest
import sort

"""Here is an example dictionary, used to test the sort functions work correctly in the sort module"""
unsortedDict = [
    {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'}, 
    {'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'}, 
    {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'}, 
    {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'}, 
    {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'}, 
    {'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'}, 
    {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'}
    ]

class TestModuleSorter(unittest.TestCase):
    def test_alphabetic_sort_desc(self):
        """ Checks sort function sorts alphabetically descending. """
        expectedOutput = [{'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'},
                          {'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedListOfDict=unsortedDict, key='Crime Category', reverse=False)
        self.assertEqual(actualOutput, expectedOutput)

    def test_alphabetic_sort_asc(self):
        """ Checks sort function sorts alphabetically ascending. """
        expectedOutput = [{'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'},
                          {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedListOfDict=unsortedDict, key='Crime Category', reverse=True)
        self.assertEqual(actualOutput, expectedOutput)

    def test_number_sort_asc(self):
        """ Checks sort function sorts numbers ascending. """
        sortedDict = []
        expectedOutput = [{'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'},
                          {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedListOfDict=unsortedDict, key='Distance (km)', reverse=False)
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_number_sort_desc(self):
        """ Checks sort function sorts numbers descending. """
        sortedDict = []
        expectedOutput = [{'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'},
                          {'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedListOfDict=unsortedDict, key='Distance (km)', reverse=True)
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_date_sort_newest(self):
        """Checks sort function accurately sorts by date and time, most recent first"""
        sortedDict = []
#2015-12 
        expectedOutput = [{'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'},
                          {'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedDict, 'Date', reverse=True, dateFormat='%Y-%m')
        self.assertEqual(actualOutput, expectedOutput)
      
    def test_distance_sort_oldest(self):
        """Checks sort function accurately sorts by date and time, oldest first"""
        sortedDict = []
        expectedOutput = [{'Distance (km)': 1.7, 'Date': '2013-11', 'Crime Category': 'Vehicle crime'},
                          {'Distance (km)': 0.6, 'Date': '2014-1', 'Crime Category': 'Anti-social behaviour'},
                          {'Distance (km)': 3.2, 'Date': '2014-2', 'Crime Category': 'Public order'},
                          {'Distance (km)': 4.4, 'Date': '2014-4', 'Crime Category': 'Shoplifting'},
                          {'Distance (km)': 1.5, 'Date': '2014-5', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 4.0, 'Date': '2014-7', 'Crime Category': 'Other crime'},
                          {'Distance (km)': 2.1, 'Date': '2015-12', 'Crime Category': 'Other theft'}]
        
    
        actualOutput = sort.listOfDictSort(unsortedDict, 'Date', reverse=False, dateFormat='%Y-%m')
        self.assertEqual(actualOutput, expectedOutput)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
