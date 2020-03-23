import unittest
import os
from writer import *

def fileReaderHelper(filepath):
    """Helper function to read files from disk to dict"""
    if os.path.exists(filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            outputArray = []
            # iterate over each row
            for row in reader:
                # setup the new row
                newRow = {}
                for key in row:
                    # add the values into the new row
                    if row[key] == None:
                        newRow[key] = ''
                    else:
                        newRow[key] = row[key]
                # add the new row to the array
                outputArray.append(newRow)
        return outputArray
    else:
        return [-1]

class TestModuleCsvToDict(unittest.TestCase):

    def test_valid_conversion(self):
        """Test to make sure that list read from new file is same as list input into writer."""
        keys = {'field1', 'field2', 'field3'}
        validContent = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'field1': 'bob10', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.csv"
        filepath = write_csv(validCsvFilename, validContent, keys)
        actualOutput = fileReaderHelper(filepath)
        expectedOutput = validContent
        self.assertEqual(actualOutput, expectedOutput)
        
    def test_invalid_input(self):
        """Test to make sure that an array containing -1 is returned if fields are different"""
        keys = {'field1', 'field2', 'field3'}
        validContent = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'test': 'test', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.csv"
        actualOutput = write_csv(validCsvFilename, validContent, keys)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_empty_input(self):
        """Test to make sure that an array containing -1 is returned if field is empty"""
        keys = {'field1', 'field2', 'field3'}
        validContent = ""
        validCsvFilename = "test.csv"
        actualOutput = write_csv(validCsvFilename, validContent, keys)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)
    
    def test_invalid_filname(self):
        """Test to make sure -1 is returned with invalid filname."""
        keys = {'field1', 'field2', 'field3'}
        validContent = [{'field1': 'bob1', 'field2': 'bob2', 'field3': 'bob3'},{'field1': 'bob10', 'field2': 'bob20', 'field3': 'bob30'},]
        validCsvFilename = "test.cv"
        actualOutput = write_csv(validCsvFilename, validContent, keys)
        expectedOutput = [-1]
        self.assertEqual(actualOutput, expectedOutput)

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()

