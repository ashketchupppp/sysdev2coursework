from modules.ui.ui import *
from modules.data.search import search_list_dict

def retrieve_crime_data(crime_data_list):
    # prompt the user to input the following: lat, long and radius
    # (pls use the ui.py module for prompting)    
    # create a second crime data list, this is the list which will be returned
    # go through the crime data list that is passed (crime_data_list)
    #   each value which is within the radius the user specified is added to the new list we just created
    # prompt the user to see if they want to sort the results 
    # if they do then sort the results using the data sorting module
    # prompt the user for a file name to write the data to
    # write the data to a csv file using the csv writer module
    pass

def find_postcode_coordinate(postcodes):
    """
    Promts user for Postcode
    Searches Postcode and prints coords
    Prints erors if multiple values found or Postcode is not found
    """
    input = prompt("Please enter a Postcode")
    search_result = search_list_dict(postcodes, input, "Postcode")
    if search_result == [-1]:
        print("No results found")
        return False
    if search_result == [-2]:
        print("Multiple results found")
        return False
    print("Lattitude: " + search_result["ETRS89GD-Lat"] + " Longitude: " + search_result["ETRS89GD-Long"])
    return True
    
    
