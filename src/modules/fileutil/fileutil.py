from pathlib import Path
import os

def find_files(dir, filetype=''):
    """ Recursively searches a directory for files matching the filetype.
        Leave empty to get a list of all files.
        Each Result item has the full path and just the filename in each result item."""
    filelist = []
    # use os.walk to create an iterable for each directory in a file tree
    for root, dirs, files in os.walk(dir):
        if len(files) > 0:
            for f in files: 
                # if the file is the right filetype or there is no filetype specified
                # then add it to the list of found files
                if f[-3:] == filetype or filetype == '':
                    filelist.append([root + '/' + f, f])
    return filelist