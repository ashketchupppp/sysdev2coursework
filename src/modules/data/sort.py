from datetime import datetime

def listOfDictSort(unsortedListOfDict, key, reverse=False, dateFormat=""):
    """ Sorts an unsorted list of dictionaries by a passed key value. """
    if dateFormat != "":
        sortedListOfDict = sorted(unsortedListOfDict, key=lambda x: datetime.strptime(x[key], dateFormat), reverse=reverse)
    else:
        sortedListOfDict = sorted(unsortedListOfDict, key = lambda i: i[key], reverse=reverse)
    return sortedListOfDict
