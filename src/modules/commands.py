#If running as main program import libraries relative to crime_data
if __name__ == "modules.commands":
    from modules.ui.cli import *
    from modules.data.search import *
    from modules.data.filter import *
    from modules.data.sort import *
    from modules.distance_between.geodist import distance
    from modules.csv.writer import *
else:
#Import libraries for testing
    from ui.cli import *
    from data.search import *
    from data.filter import *
    from data.sort import *
    from csv.writer import *
    from distance_between.geodist import distance

def retrieve_crime_data(crime_data_list):
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
        filtered_data = filterData(crime_data, postcodelatlng, radius)
        input = prompt("How would you like the data sorted? (crime category, date (recent first), distance)" )
        if input == "crime category":
            key = "Crime type"
            reverse = False
        elif input == "date":
            key = "Month"
            reverse = True
        elif input == "distance":
            key = "distance_between"
            reverse = False
        
        sorted_data = listOfDictSort(filtered_data, key, reverse, dateFormat="")
        
        
        filepath = "empty.csv"
        input = prompt("What should the report be called?")
        filepath = input + ".csv"
        dict_to_csv(filepath, sorted_data)
        print("Report created in " + filepath)
        

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
