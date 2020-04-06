if __name__ == "modules.data.filter":
    from modules.geodist.geodist import distance
else:
#Import libraries for testing
    import sys
    import os
    sys.path.insert(0, os.getcwd() + '/../')
    
    from geodist.geodist import distance
    
def filterData(dictList, postcodelatlng, radius):
    """Function to filter the given data using the given values."""
    result = []
    for crime_record in dictList:
        try:
            crimelatlng = []
            crimelatlng.append(float(crime_record["Latitude"]))
            crimelatlng.append(float(crime_record["Longitude"]))
            geodist = distance(postcodelatlng, crimelatlng)
            if int(geodist) < radius:
                crime_record['Distance'] = geodist
                result.append(crime_record)
        except:
            error = 1
    return result
   