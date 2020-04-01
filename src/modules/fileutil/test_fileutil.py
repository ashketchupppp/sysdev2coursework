import unittest
import shutil
import os
from fileutil import *

def directoryCreatorHelper(filelist):
    """Creates a set of directories and files to test the recursive file searcher."""
    cwd = os.getcwd()
    for item in filelist:
        if item[-1] == "/":
            os.mkdir(cwd + "/" + item)
        else:
            tempfile = open(cwd +  "/" + item, "w")
            tempfile.close()

def directoryDeleterHelper(directory):
    """Deletes the set of directories and files created by the directoryCreatorHelper."""
    shutil.rmtree(directory)

class TestRecursiveFileSearch(unittest.TestCase):
    def test_nofilter(self):
        """Test to make sure it correctly identifies all files and directories."""
        os.mkdir('./testdir')
        dirsandfiles = ['testdir/testdir2/', "testdir/csvfile.csv", "testdir/testdir2/xmlfile.xml"]
        cwd = os.getcwd()
        for dirorfile in dirsandfiles:
            dirorfile = cwd + "/" + dirorfile

        directoryCreatorHelper(dirsandfiles)
        result = recursive_search(cwd + "/testdir")
        directoryDeleterHelper(cwd + '/testdir')
        self.assertEqual(result, dirsandfiles)

        


    def test_filter(self):
        """Test to make sure it correctly filters some files out"""
        pass
    
# this is required to be able to run the tests
if __name__ == '__main__':
    unittest.main()