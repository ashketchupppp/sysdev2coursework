from modules.ui import *
import sys, os
sys.path.append('../distance_between')
import geodist

def retrieve_crime_data(crime_data_list):
    dist = geodist.distance((51.295341, 0.165940), (51.294180, 0.166670))
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
    # prompt the user to input the following: a postcode
    # (pls use the ui.py module for prompting)
    # use the search function in the data searching module to find a postcode
    # if one is found
    #   output the lat and long
    # if one is not found
    #   tell the user the postcode could not be found
    pass
