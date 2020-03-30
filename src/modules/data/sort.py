from datetime import datetime

# if you are sorting a date then just pass a value for dateFormat
# if you are trying to use this function I would recommend looking at the tests
# to see how to use it
def listOfDictSort(unsortedListOfDict, key, reverse=False, dateFormat=""):
    """ Sorts an unsorted list of dictionaries by a passed key value. """
    if dateFormat != "":
        sortedListOfDict = sorted(unsortedListOfDict, key=lambda x: datetime.strptime(x[key], dateFormat), reverse=reverse)
    else:
        sortedListOfDict = sorted(unsortedListOfDict, key = lambda i: i[key], reverse=reverse)
    return sortedListOfDict
