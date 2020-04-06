import unittest
import os
import sys
from writer import *
sys.path.insert(0, os.getcwd() + '/../')
#Helper function to read files from disk to dict, has its own tests
from fileread.reader import csv_to_dict as fileReaderHelper


class TestModuleCsvToDict(unittest.TestCase):

    def test_valid_conversion(self):
        """Test to make sure that list read from new file is same as list input into writer."""
        validDict = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'field1': 'bob10', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.csv"
        filepath = dict_to_csv(validCsvFilename, validDict)
        actualOutput = fileReaderHelper(filepath)
        expectedOutput = validDict
        self.assertEqual(actualOutput, expectedOutput)

    def test_invalid_input(self):
        """Test to make sure that an array containing -1 is returned if fields are different"""
        validDict = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'test': 'test', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.csv"
        actualOutput = dict_to_csv(validCsvFilename, validDict)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)

    def test_empty_input(self):
        """Test to make sure that an array containing -1 is returned if field is empty"""
        validDict = ""
        validCsvFilename = "test.csv"
        actualOutput = dict_to_csv(validCsvFilename, validDict)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)

    def test_invalid_filname(self):
        """Test to make sure that list read from new file is same as list input into writer."""
        validDict = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'field1': 'bob10', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.cv"
        actualOutput = dict_to_csv(validCsvFilename, validDict)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)
        
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()