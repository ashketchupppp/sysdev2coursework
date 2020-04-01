#If running as main program import libraries relative to crime_data
if __name__ == "modules.commands":
    from modules.ui.cli import *
    from modules.data.search import *
else:
#Import libraries for testing
    from ui.cli import *
    from data.search import *

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

def find_postcode_coordinate(postcode, data):
    search_result = search_list_dict(data, postcode, "Postcode")
    if search_result == [-1]:
        return -1
    elif search_result == [-2]:
        return -2
    return search_result["ETRS89GD-Lat"] + search_result["ETRS89GD-Long"]

class CmdRetrieveCrimeData(Command):
    def __init__(self, commandLine):
        """ Constructor method. Calls parent class constructor. """
        helpmessage = "Search for crime data, save it to csv and optionally sort it."
        Command.__init__(self, 'crimedata', ['crimedata'], commandLine, helpmessage)
    
    def commandBody(self, variables):
        """ Docstrings woo """
        # put your bullshit here
        pass

class CmdPostcodeFromCoordinate(Command):
    def __init__(self, commandLine):
        """ Constructor method. Calls parent class constructor. """
        helpMessage = 'Search for the co-ordinates of a postcode'
        Command.__init__(self, 'postcode', ['postcodes'], commandLine, helpMessage)
        
    def commandBody(self, variables):
        """
        Promts user for Postcode
        Searches Postcode and prints coords
        Prints erors if multiple values found or Postcode is not found
        """

        input = self.prompt("Please enter a Postcode")
        result = find_postcode_coordinate(input, variables['postcodes'])
        if result == -1:
            print("No results found")
        elif result == -2:
            print("Multiple results found")
        else:
            print("Latitude: " + result["ETRS89GD-Lat"] + " Longitude: " + result["ETRS89GD-Long"])
