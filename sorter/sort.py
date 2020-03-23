from datetime import datetime

""" Please note I have used unsortedDict as the name of the unsorted dictionary
    The dictionary should be changed to the appropriate name outputted from
    the filter module"""

def sortDate(reverse):
    """ When reverse=True, data will be sorted by most recent first"""
    sortedDict = sorted(unsortedDict, key=lambda x: datetime.strptime(x['Date'], '%d/%m/%y %H:%M'), reverse=reverse)
    return sortedDict


def sortDistCrime(type, reverse):
    """ When reverse=True, data will be sorted by reverse alphabetical order for Crime Category
        or by crime furthest away from Postcode first  
    """
    sortedDict = sorted(unsortedDict, key = lambda i: i[type], reverse=reverse)
    return sortedDict


