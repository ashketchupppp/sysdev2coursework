from datetime import datetime

# if you are sorting a date then just pass a value for dateFormat
# if you are trying to use this function I would recommend looking at the tests
# to see how to use it
def listOfDictSort(unsortedListOfDict, key, reverse=False, dateFormat=""):
    """ Sorts an unsorted list of dictionaries by a passed key value. """
    if dateFormat != "":
        # sorted returns a sorted list from the items in an iterable
        # here we use a lambda function as a quick way of creating a function
        # then we pass the function as the 'key' argument in the 'sorted' function
        # which will then apply the key argument function to each element in the unsortedListOfDict
        sortedListOfDict = sorted(unsortedListOfDict, key = lambda x: datetime.strptime(x[key], dateFormat), reverse = reverse)
    else:
        sortedListOfDict = sorted(unsortedListOfDict, key = lambda i: i[key], reverse = reverse)
    return sortedListOfDict
