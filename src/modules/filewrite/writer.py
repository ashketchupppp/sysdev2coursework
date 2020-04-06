import csv
import os

def dict_to_csv(filepath, content):
    """Writes contents of a dictionary to a .csv file"""
    #Check if the file is a csv file, return if not
    if filepath[-4:] != ".csv":
        print("Not csv file")
        return [-1]
    #Checking content type, retun if invalid
    if not isinstance(content,(list,dict)):
        print("Not List or Dictionary")
        return [-1]
    #Create list of keys, for headings
    keys = content[0].keys()
    #Catch exceptions and return -1 -error
    try:
        with open(filepath, 'w', newline="") as csv_file:
            dict_writer = csv.DictWriter(csv_file, keys)  
            dict_writer.writeheader() #Add the csv Headers
            dict_writer.writerows(content) #write content on each line
        return filepath #return the written file
    except Exception:
        return [-1]