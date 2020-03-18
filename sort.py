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

def distsort():
    #function to sort by distance from postcode
    sortedDict = sorted(unsortedDict, key = lambda i: i['Distance (km)'])
    print(sortedDict)
    
def datesort():
    #function to sort by date (recent first)
    from datetime import datetime

    sortedDict = sorted(
    unsortedDict,
    key=lambda x: datetime.strptime(x['Date'], '%d/%m/%y %H:%M'), reverse=True
    )
    print(sortedDict)
    
def crimesort():
    #function to sort date by crime category 
    sortedDict = sorted(unsortedDict, key = lambda i: i['Crime Category'])
    print(sortedDict)
    
print("Data sorted by distance from postcode")
distsort()
print()
print("Data sorted by date (most recent first)")
datesort()
print()
print("Data sorted by crime category")
crimesort()