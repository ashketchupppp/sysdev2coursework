import unittest
import shutil
import os
from fileutil import *

def directoryCreatorHelper(dirs, filelist):
    """Creates a set of directories and files to test the recursive file searcher."""
    cwd = os.getcwd()
    for dir in dirs:
        try:
            os.makedirs(f'{cwd}/{dir}')
        except Exception as e:
            # dir already exists
            print(e)
    for item in filelist:
        file = open(item, "x")
        file.close()

class TestRecursiveFileSearch(unittest.TestCase):
    files = ["testdir/csvfile.csv", "testdir/testdir2/xmlfile.xml"]
    dirs = ['/testdir/testdir2/']
    
    def createTestDirs(self):
        """ Create the test directories. """
        # create the directories, we don't know the absolute path so build it from
        # the relative paths in the list
        cwd = os.getcwd()
        newfilelist = []
        for file in TestRecursiveFileSearch.files:
            newfilelist.append(cwd + "/" + file)
        directoryCreatorHelper(TestRecursiveFileSearch.dirs, newfilelist)
            
    def deleteTestDir(self):
        """ Delete the test directory """
        shutil.rmtree(os.getcwd() + '/testdir')
    
    def setUp(self):
        self.createTestDirs()
        
    def tearDown(self):
        self.deleteTestDir()
        
    def test_nofilter(self):
        """Test to make sure it correctly identifies all files."""        
        # convert absolute path to relative path
        cwd = os.getcwd()
        result = find_files(cwd + "/testdir/")
        
        # format the result so we can compare it to the TestRecursiveFileSearch.files variable
        for pos in range(len(result)):
            result[pos] = result[pos][0][len(cwd) + 1:]
        
        # remove all double slashes incase windows decides to add them
        for pos in range(len(result)):
            result[pos] = result[pos].replace('//', '/')
            
        self.assertEqual(result, TestRecursiveFileSearch.files)
        
    def test_filter(self):
        """Test to make sure it correctly identifies all csv files."""        
        # convert absolute path to relative path
        cwd = os.getcwd()
        result = find_files(cwd + "/testdir/")
        
        # format the result so we can compare it to the TestRecursiveFileSearch.files variable
        for pos in range(len(result)):
            result[pos] = result[pos][0][len(cwd) + 1:]
        
        # remove all double slashes incase windows decides to add them
        for pos in range(len(result)):
            result[pos] = result[pos].replace('//', '/')
        
        correctResult = [TestRecursiveFileSearch.files[0]]
        self.assertEqual(result, TestRecursiveFileSearch.files)
        

# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()