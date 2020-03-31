#If running as main program import libraries relative to crime_data
if __name__ == "modules.commands":
    from modules.ui.ui import *
    from modules.data.search import *
    from modules.data.filter import *
    from modules.data.sort import *
    from modules.distance_between.geodist import distance
    from modules.csv.writer import *
else:
#Import libraries for testing
    from ui.ui import *
    from data.search import *
    from data.filter import *
    from data.sort import *
    from csv.writer import *
    from distance_between.geodist import distance
    
def retrieve_crime_data(postcodes, crime_data):
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
    lat = search_result["ETRS89GD-Lat"]
    long = search_result["ETRS89GD-Long"]
    postcodelatlng = []
    postcodelatlng.append(float(lat))
    postcodelatlng.append(float(long))
    print(postcodelatlng)
    print(lat + ", " + long)
    input = prompt("Please enter a search radius in km")
    radius = int(input)
    input = prompt("How would you like the data sorted?")
    key = input
    
    filtered_data = filterData(crime_data, postcodelatlng, radius, key)
    filepath = "empty.csv"
    input = prompt("What should the report be called?")
    filepath = input + ".csv"
    dict_to_csv(filepath, filtered_data)
    print("Report created in " + filepath)
   
        
    # prompt the user to input the following: lat, long and radius
    # (pls use the ui.py module for prompting)    
    # create a second crime data list, this is the list which will be returned
    # go through the crime data list that is passed (crime_data_list)
    #   each value which is within the radius the user specified is added to the new list we just created
    # prompt the user to see if they want to sort the results 
    # if they do then sort the results using the data sorting module
    # prompt the user for a file name to write the data to
    # write the data to a csv file using the csv writer module
   

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
    return search_result["ETRS89GD-Lat"] + search_result["ETRS89GD-Long"]