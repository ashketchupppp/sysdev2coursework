from libs.Crime_Search import search_files 
from libs.postcodes import find_coords

postcode = input('Enter postcode to find\n')
radiusinp = input('Enter rasius to find results for\n')
radius = int(radiusinp)
lat1, lon1 = find_coords(postcode)
result = search_files(lat1, lon1, radius)
#print(result)