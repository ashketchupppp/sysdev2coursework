import csv
import os

def dict_to_csv(filepath, content):
    """Writes contents of a dictionary to a .csv file"""
    #Check if filepath is csv file, return if not
    if filepath[-4:] != ".csv":
        print("Not csv file")
        return [-1]
    #Checking content type, return if invalid
    if not isinstance(content,(list,dict)):
        print("Not List or Dictionary")
        return [-1]
    #Create list of keys, for headings
    keys = content[0].keys()
    try:
        #Write header + rows to file
        with open(filepath, 'w', newline="") as csv_file:
            dict_writer = csv.DictWriter(csv_file, keys)  
            dict_writer.writeheader() 
            dict_writer.writerows(content)
        #return the written file
        return filepath 
    except Exception:
        return [-1]