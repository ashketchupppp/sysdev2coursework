import unittest
from filter import filterData
#Test requires importing functions for the main function to work
#These functions are all individualy tested
#Dictlist is small sample of test Data
def get_dict_list():
    """Small sample of test data, individually checked"""
    test_data = [{'Crime ID': '1', 'Longitude': '-4.543798', 'Latitude': '50.830723'},
        {'Crime ID': '2', 'Longitude': '-4.544117', 'Latitude': '50.827973'},
        {'Crime ID': '3', 'Longitude': '-4.548403', 'Latitude': '50.828185'},
        {'Crime ID': '4', 'Longitude': '-4.551129', 'Latitude': '50.828441'},
        {'Crime ID': '5', 'Longitude': '-4.551129', 'Latitude': '50.828441'},]
    return test_data

class TestFilter(unittest.TestCase):
    def test_working_multiple(self):
        """Testing that the filter return the expected results with valid data"""
        postcodelatlng = [50.827973, -4.543798]
        radius = 10
        dictList = get_dict_list()
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = [{'Crime ID': '1', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Distance': 0.3057864802417903},
                          {'Crime ID': '2', 'Longitude': '-4.544117', 'Latitude': '50.827973', 'Distance': 0.022405434837250257},
                          {'Crime ID': '3', 'Longitude': '-4.548403', 'Latitude': '50.828185', 'Distance': 0.32429614137803187},
                          {'Crime ID': '4', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Distance': 0.5175240380244737},
                          {'Crime ID': '5', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Distance': 0.5175240380244737}]
        self.assertEqual(actualOutput, expectedOutput)

    def test_radius(self):
        """Testing that the filter returns empty list when radius is 0"""
        dictList = get_dict_list()
        postcodelatlng = [50.827974, -4.543799]
        radius = 0
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)

    def test_working_single(self):
        """Testing that the filter returns the expected results with only one input"""
        test_data = get_dict_list()
        dictList = [test_data[0]]
        postcodelatlng = [51.830723, -4.543798]
        radius = 1000
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = [{'Crime ID': '1', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Distance': 111.19508372419087}]
        self.assertEqual(actualOutput, expectedOutput)

    def test_empty_input(self):
        """Testing that the filter returns the expected results with only one input"""
        #Testing Empty input
        dictList = []
        postcodelatlng = [50.830723, -4.543798]
        radius = 100
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)

    def test_same_coord(self):
        """Testing one result returned if radius is 0 and input empty"""
        #Testing Empty input
        dictList = []
        postcodelatlng = [51.830723, -4.543798]
        radius = 0
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)

    def test_not_list(self):
        """Testing that empty list retunred if input is not a list - not error"""
        test_data = get_dict_list()
        dictList = test_data[0]
        postcodelatlng = [50.830723, -4.543798]
        radius = 1000
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()