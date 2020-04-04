import unittest
from data.filter import filterData
#Test requires importing functions for the main function to work
#These functions are all individualy tested
#Dictlist is small sample of test Data
dictList = [{'Crime ID': '2de16765bdc8eb5f071bc10bfa421729a55fdb60a15a4cb4099a0576dc313b42', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Location': 'On or near Shopping Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Burglary', 'Last outcome category': 'Unable to prosecute suspect', 'Context': ''},
        {'Crime ID': 'd6aea8c1149f538afa2c88b4ec73f019a89e6dae41aae7afa740825019af375c', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.544117', 'Latitude': '50.827973', 'Location': 'On or near The Strand', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Possession of weapons', 'Last outcome category': 'Status update unavailable', 'Context': ''},
        {'Crime ID': '6cbf83a2c22b130ea764aa8717bdec4ad92b8dfeb37f12a2a3adf218deaffac7', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.548403', 'Latitude': '50.828185', 'Location': 'On or near Parking Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Public order', 'Last outcome category': 'Investigation complete; no suspect identified', 'Context': ''},
        {'Crime ID': 'bdad97231460e13410876599a80cb0b59f8040ea4ec9edb81286fe8a4e5c7a05', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Location': 'On or near Church Path', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Public order', 'Last outcome category': 'Unable to prosecute suspect', 'Context': ''},
        {'Crime ID': '1c67777f9add8fecfc564b6375a5e23732617c87709a9d05e15808ac1af4f918', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Location': 'On or near Church Path', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Violence and sexual offences', 'Last outcome category': 'Investigation complete; no suspect identified', 'Context': ''},]
class TestFilter(unittest.TestCase):
    def test_working_multiple(self):
        """Testing that the filter return the expected results with valid data"""
        postcodelatlng = [50.827973, -4.543798]
        radius = 10
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = [{'Crime ID': '2de16765bdc8eb5f071bc10bfa421729a55fdb60a15a4cb4099a0576dc313b42', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Location': 'On or near Shopping Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Burglary', 'Last outcome category': 'Unable to prosecute suspect', 'Context': '', 'Distance': 0.3057864802417903},
                          {'Crime ID': 'd6aea8c1149f538afa2c88b4ec73f019a89e6dae41aae7afa740825019af375c', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.544117', 'Latitude': '50.827973', 'Location': 'On or near The Strand', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Possession of weapons', 'Last outcome category': 'Status update unavailable', 'Context': '', 'Distance': 0.022405434837250257},
                          {'Crime ID': '6cbf83a2c22b130ea764aa8717bdec4ad92b8dfeb37f12a2a3adf218deaffac7', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.548403', 'Latitude': '50.828185', 'Location': 'On or near Parking Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Public order', 'Last outcome category': 'Investigation complete; no suspect identified', 'Context': '', 'Distance': 0.32429614137803187},
                          {'Crime ID': 'bdad97231460e13410876599a80cb0b59f8040ea4ec9edb81286fe8a4e5c7a05', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Location': 'On or near Church Path', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Public order', 'Last outcome category': 'Unable to prosecute suspect', 'Context': '', 'Distance': 0.5175240380244737},
                          {'Crime ID': '1c67777f9add8fecfc564b6375a5e23732617c87709a9d05e15808ac1af4f918', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.551129', 'Latitude': '50.828441', 'Location': 'On or near Church Path', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Violence and sexual offences', 'Last outcome category': 'Investigation complete; no suspect identified', 'Context': '', 'Distance': 0.5175240380244737}]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_radius(self):
        """Testing that the filter returns empty list when radius is 0"""
        postcodelatlng = [50.827974, -4.543798]
        radius = 0
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_working_single(self):
        """Testing that the filter returns the expected results with only one input"""
        dictList = [{'Crime ID': '2de16765bdc8eb5f071bc10bfa421729a55fdb60a15a4cb4099a0576dc313b42', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Location': 'On or near Shopping Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Burglary', 'Last outcome category': 'Unable to prosecute suspect', 'Context': ''}]
        postcodelatlng = [51.830723, -4.543798]
        radius = 1000
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = [{'Crime ID': '2de16765bdc8eb5f071bc10bfa421729a55fdb60a15a4cb4099a0576dc313b42', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Location': 'On or near Shopping Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Burglary', 'Last outcome category': 'Unable to prosecute suspect', 'Context': '', 'Distance': 111.19508372419087}]
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_empty_input(self):
        """Testing that the filter returns the expected results with only one input"""
        dictList = []
        postcodelatlng = [50.830723, -4.543798]
        radius = 100
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_same_coord(self):
        """Testing one result returned if radius is 0 and input empty"""
        dictList = []
        postcodelatlng = [51.830723, -4.543798]
        radius = 0
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_not_list(self):
        """Testing that empty list retunred if input is not a list - not error"""
        dictList = {'Crime ID': '2de16765bdc8eb5f071bc10bfa421729a55fdb60a15a4cb4099a0576dc313b42', 'Month': '2019-01', 'Reported by': 'Devon & Cornwall Police', 'Falls within': 'Devon & Cornwall Police', 'Longitude': '-4.543798', 'Latitude': '50.830723', 'Location': 'On or near Shopping Area', 'LSOA code': 'E01018936', 'LSOA name': 'Cornwall 001A', 'Crime type': 'Burglary', 'Last outcome category': 'Unable to prosecute suspect', 'Context': ''}
        postcodelatlng = [50.830723, -4.543798]
        radius = 1000
        actualOutput = filterData(dictList, postcodelatlng, radius)
        expectedOutput = []
        self.assertEqual(actualOutput, expectedOutput)
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
