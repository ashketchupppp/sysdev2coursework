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
        Prompts user for a postcode and finds centre coordinate of that postcode
        Prompts user for a radius and filters crime data within that radius of postcode centre
        Prompts user for method of sorting data
        Prompts user for file name for CSV
        Results are outputted into CSV with specified file name
        Uses are re-prompted if invalid information is inputted
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
            input = self.prompt('''How would you like the data sorted? Enter the number you would like to select.
1. crime category
2. date (most recent first)
3. distance
4. no sort''')
            # check it is a number
            try:
                numberSelected = int(input) - 1
            except:
                print('That is not a number.')
                raise Exception('restart')
            
            # check it is a valid number
            if numberSelected > 3 or numberSelected < 0:
                print('That is not a number on the list.')
                raise Exception('restart')
            
            # setup the valid values and check against them
            data_field_values = ['Crime type', 'Month', 'Distance']
            data_field_sort_direction = [False, True, False]
            sorted_data = filtered_data
            if numberSelected == 3:
                sorted_data = filtered_data    
            elif numberSelected == 0 or numberSelected == 2:
                # sorting by non-date values
                sorted_data = listOfDictSort(filtered_data, data_field_values[numberSelected], reverse = data_field_sort_direction[numberSelected], dateFormat="")
            elif numberSelected == 1:
                # sorting by date value
                sorted_data = listOfDictSort(filtered_data, data_field_values[numberSelected], reverse = data_field_sort_direction[numberSelected], dateFormat="%Y-%m")
            print(len(sorted_data))
            # save the report to csv
            filepath = "default.csv"
            input = self.prompt("What should the report be called?")
            filepath = input + ".csv"
            dict_to_csv(filepath, sorted_data)
            print("Report created in " + filepath)
