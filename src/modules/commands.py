#If running as main program import libraries relative to crime_data
if __name__ == "modules.commands":
    from modules.ui.cli import *
    from modules.data.search import *
    from modules.data.filter import *
    from modules.data.sort import *
    from modules.geodist.geodist import distance
    from modules.filewrite.writer import *
else:
#Import libraries for testing
    from ui.cli import *
    from data.search import *
    from data.filter import *
    from data.sort import *
    from filewrite.writer import *
    from geodist.geodist import distance

def find_postcode_coordinate(postcode, data):
    search_result = search_list_dict(data, postcode, "Postcode")
    if search_result == [-1]:
        return -1
    elif search_result == [-2]:
        return -2
    lat_long = [search_result["ETRS89GD-Lat"], search_result["ETRS89GD-Long"]]
    return lat_long

class CmdRetrieveCrimeData(Command):
    def __init__(self, commandLine):
        """ Constructor method. Calls parent class constructor. """
        helpmessage = "Search for crime data, save it to csv and optionally sort it."
        Command.__init__(self, 'crimedata', ['crimedata', 'postcodes'], commandLine, helpmessage)
    
    def commandBody(self, variables):
        """
        Prompts user for a postcode and finds centre coordinate of that postcode
        Prompts user for a radius and filters crime data within that radius of postcode centre
        Prompts user for method of sorting data
        Prompts user for file name for CSV
        Results are outputted into CSV with specified file name
        Uses are re-prompted if invalid information is inputted
        """
        while True:
            try:
                input = self.prompt("Please enter a Postcode")
                result = find_postcode_coordinate(input, variables['postcodes'])
            except ValueError:
                print("Sorry, that is an invalid postcode")
                continue
            if result == -1:
                print("Could not find postcode")
                continue
            elif result == -2:
                print("Multiple postcodes found")
                continue
            else:
                print("Latitude: " + result[0] + " Longitude: " + result[1])
                lat = result[0]
                long = result[1]
                postcodelatlong = []
                postcodelatlong.append(float(lat))
                postcodelatlong.append(float(long))
                break
            
        while True:
            try:
                input = self.prompt("Please enter a search radius in km")
                radius = int(input)
            except ValueError:
                print("Sorry, that is an invalid radius")
                continue
            if input <= "0":
                print("Sorry, that is an invalid radius")
                continue
            else:
                break
        filtered_data = filterData(variables['crimedata'], postcodelatlong, radius)
        
        while True:
            try:
                input = self.prompt("How would you like the data sorted? By crime category, date (recent first) or distance?" )
            except ValueError:
                print("Sorry, that is an invalid sort type")
                continue
            if input not in ("crime category", "date", "distance"):
                print("Please enter a valid sort type")
            else:
                break 
        if input == "crime category":
            key = "Crime type"
            reverse = False
        elif input == "date":
            key = "Month"
            reverse = True
        elif input == "distance":
            key = "Distance"
            reverse = False
            
        sorted_data = listOfDictSort(filtered_data, key, reverse, dateFormat="")
        filepath = "empty.csv"
        input = self.prompt("What should the report be called?")
        filepath = input + ".csv"
        dict_to_csv(filepath, sorted_data)
        print("Report created in " + filepath)
