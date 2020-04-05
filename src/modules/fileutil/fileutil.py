from pathlib import Path
import os

def recursive_search(directory, wildcard="*"):
    """Recursively search a directory for files matching the given wildcard."""
    results  = []
    for path in Path(directory).rglob(wildcard):
        results.append(path) 
    return results

def find_files(dir, filetype=''):
    """ Recursively searches a directory for files matching the filetype.
        Leave empty to get a list of all files.
        Each Result item has the full path and just the filename in each result item."""
    filelist = []
    for root, dirs, files in os.walk(dir):
        if len(files) > 0:
            for f in files: 
                if f[-3:] == filetype or filetype == '':
                    filelist.append([root + '/' + f, f])
    return filelist
    