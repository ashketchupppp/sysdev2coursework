if __name__ == "modules.data.filter":
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
    
def filterData(dictList, postcodelatlng, radius):
    """Function to filter the given data using the given values."""
    result = []
    for crime_record in dictList:
        try:
            crimelatlng = []
            crimelatlng.append(float(crime_record["Latitude"]))
            crimelatlng.append(float(crime_record["Longitude"]))
            distance_between = distance(postcodelatlng, crimelatlng)
            if int(distance_between) < radius:
                result.append(crime_record.copy())
        except:
            error = 1
    return result
   