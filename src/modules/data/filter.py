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
    #create empty list
    result = []
    #each dict in the list
    for crime_record in dictList:
        try:
            crimelatlng = []#empty list
            crimelatlng.append(float(crime_record["Latitude"])) #adding lat
            crimelatlng.append(float(crime_record["Longitude"]))#adding long
            geodist = distance(postcodelatlng, crimelatlng) #lookup distance between two coords
            #if distance between the results is greter than users radius, then add result to list
            if int(geodist) < radius:
                crime_record['Distance'] = geodist
                result.append(crime_record)
        except:
            #catching error, used for testing
            error = 1 
    return result
   