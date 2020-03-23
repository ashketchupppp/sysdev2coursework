from datetime import datetime
#Below is example data Ive used to help test this module
unsortedDict = [
      {'Distance (km)': 2.1, 'Date': '12/12/15 15:01', 'Crime Category': 'Other theft'}, 
      {'Distance (km)': 0.6, 'Date': '1/1/14 18:21', 'Crime Category': 'Anti-social behaviour'}, 
      {'Distance (km)': 1.5, 'Date': '10/5/14 22:41', 'Crime Category': 'Other crime'}, 
      {'Distance (km)': 4.4, 'Date': '1/4/14 18:20', 'Crime Category': 'Shoplifting'}, 
      {'Distance (km)': 3.2, 'Date': '2/2/14 23:05', 'Crime Category': 'Public order'}, 
      {'Distance (km)': 1.7, 'Date': '9/11/13 9:02', 'Crime Category': 'Vehicle crime'}, 
      {'Distance (km)': 4.0, 'Date': '30/7/14 11:28', 'Crime Category': 'Other crime'}
    ]

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


print(sortDate(True))
print()
print(sortDistCrime('Distance (km)', True))
