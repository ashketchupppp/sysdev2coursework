if __name__ == "modules.data.filter":
    from modules.geodist.geodist import distance
else:
#Import libraries for testing
    import sys
    import os
    sys.path.insert(0, os.getcwd() + '/../')
    
    from geodist.geodist import distance
    
def filterData(dictList, postcodelatlng, radius):
    """Function to filter the given list of dictionaries by the user defined radius from the centre coordinate of a postcode."""
    result = []
    #For each dict in the list
    for crime_record in dictList:
        try:
            #Create list with [lat, long]
            crimelatlng = []
            crimelatlng.append(float(crime_record["Latitude"])) 
            crimelatlng.append(float(crime_record["Longitude"]))
            #lookup distance between two coords
            geodist = distance(postcodelatlng, crimelatlng) 
            #Add crime if distance less than user's radius
            if int(geodist) < radius:
                crime_record['Distance'] = geodist
                result.append(crime_record)
        except:
            #catching error, used for testing
            error = 1 
    return result
   