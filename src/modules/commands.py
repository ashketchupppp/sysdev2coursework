if __name__ == "modules.commands":
    #If running as main program import libraries relative to crime_data
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
    """ Finds a particular postocde co-rdinate using from the data variable """
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
        Promts user for Postcode
        Searches Postcode and prints coords
        Prints erors if multiple values found or Postcode is not found
        """

        # prompt for a postcode
        input = self.prompt("Please enter a Postcode")
        result = find_postcode_coordinate(input, variables['postcodes'])
        if result == -1:
            print("Could not find postcode")
        elif result == -2:
            print("Multiple postcodes found")
        else:
            # print lat and long incase they want it
            print("Latitude: " + result[0] + " Longitude: " + result[1])
            input = self.prompt("Please enter an integer search radius in kilometers")
            
            # perform some validation
            try:
                radius = int(input)
            except ValueError:
                print('That is not a valid integer.')
                raise Exception('restart')
            if radius <= 0:
                print('Radius must be larger than 0')
                raise Exception('restart')
            
            # if we get to here then the radius is valid, call the filter function
            filtered_data = filterData(variables['crimedata'], [float(result[0]), float(result[1])], radius)
            input = self.prompt('How would you like the data sorted? By "crime category", "date" (recent first), "distance" or "no sort"?' )
            # setup the valid values and check against them
            valid_values = {'crime cateogry':['Crime type', False], 'date' : ['Month', True], 'distance' : ['Distance', False], 'no sort':False}
            
            if input not in valid_values:
                print('That was not one of "crime category", "date" or "distance"')
                raise Exception('restart')
            elif valid_values[input] != False:
                # sort the data
                sorted_data = listOfDictSort(filtered_data, valid_values[input][0], valid_values[input][1], dateFormat="")
            
            # save the report to csv
            filepath = "default.csv"
            input = self.prompt("What should the report be called?")
            filepath = input + ".csv"
            dict_to_csv(filepath, sorted_data)
            print("Report created in " + filepath)