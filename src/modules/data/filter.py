def filter(dictList, radius):
    """Function to filter the given data using the given values."""
    filteredDict = [d for d in dictList if d['distance'] <= radius]
    return filteredDict
    # this should use the distance between module to figure out if a coord is within the radius or not 
    # read the git issue to see exactly what this needs to do im not typing it out again
