import unittest
import os
from reader import *

def fileWriteHelper(string, filename):
    """Helper function to write files to disk."""
    # open a new file and write the string to it
    file = open(filename, "w")
    file.write(string)
    file.close()

def fileDeleteHelper(filename):
    """Helper function to delete files from the disk."""
    # check the file exists to prevent errors
    if os.path.exists(filename):
        os.remove(filename) 

class TestModuleCsvToDict(unittest.TestCase):

    def test_valid_conversion(self):
        """Test to make sure that a completely populated csv file is read correctly."""
        validCsvString = "firstName,lastName,dateofbirth,numberofsiblings\ndave,lloyd,14/01/2000,0\njack,nicks,06/04/2001,1\njill,nicks,06/04/2001,1\n"

        expectedOutput = [
                {"firstName":"dave", "lastName":"lloyd", "dateofbirth":"14/01/2000", "numberofsiblings":"0"},
                {"firstName":"jack", "lastName":"nicks", "dateofbirth":"06/04/2001", "numberofsiblings":"1"},
                {"firstName":"jill", "lastName":"nicks", "dateofbirth":"06/04/2001", "numberofsiblings":"1"}
        ]

        validCsvFilename = "test.csv"
        fileWriteHelper(validCsvString, validCsvFilename)
        actualOutput = csv_to_dict(validCsvFilename)
        fileDeleteHelper(validCsvFilename)
        self.assertEqual(actualOutput, expectedOutput)

    def test_converts_blank_values(self):
        """Test to make sure that a csv file with empty values will produce a row with empty values instead of omitting the key."""
        validCsvString = "firstName,lastName,dateofbirth,numberofsiblings\n,lloyd,14/01/2000,0\njack,,06/04/2001,1\njill,nicks,,\n"

        expectedOutput = [
                {"firstName":"", "lastName":"lloyd", "dateofbirth":"14/01/2000", "numberofsiblings":"0"},
                {"firstName":"jack", "lastName":"", "dateofbirth":"06/04/2001", "numberofsiblings":"1"},
                {"firstName":"jill", "lastName":"nicks", "dateofbirth":"", "numberofsiblings":""}
        ]

        validCsvFilename = "test.csv"
        fileWriteHelper(validCsvString, validCsvFilename)
        actualOutput = csv_to_dict(validCsvFilename)
        fileDeleteHelper(validCsvFilename)
        self.assertEqual(actualOutput, expectedOutput)

    def test_no_throw_on_nonexistent_file(self):
        """Test to make sure that an array containing a -1 is returned when a csv file does not exist."""
        expectedOutput = [-1]
        invalidCsvFilename = "test.csv"
        actualOutput = csv_to_dict(invalidCsvFilename)
        self.assertEqual(actualOutput, expectedOutput)
        
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()
