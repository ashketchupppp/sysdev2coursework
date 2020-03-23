import csv
import os

def write_csv(filepath, content, keys):
    """Writes contents of a csv fomatted string to a .csv file"""
    #Check if the filname is valid
    if filepath[-4:] != ".csv":
        print("Not csv file")
        return [-1]
    #Check if content is blank
    if content == "":
        print("Content empty")
        return [-1]
    #Write to the csv file
    try:
        with open(filepath, 'w', newline="") as csv_file: 
            dict_writer = csv.DictWriter(csv_file, keys)
            dict_writer.writeheader() #Write the keys
            dict_writer.writerows(content) #loop through each row
        return filepath #return the written file
    except Exception:
        return [-1]
    
def csv_to_dict(filepath):
    """Reads a .csv file and outputs the contents into list of strings."""
    if os.path.exists(filepath):
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            outputArray = []
            # iterate over each row
            for row in reader:
                # setup the new row
                newRow = {}
                for key in row:
                    # add the values into the new row
                    if row[key] == None:
                        newRow[key] = ''
                    else:
                        newRow[key] = row[key]
                # add the new row to the array
                outputArray.append(newRow)
        return outputArray
    else:
        return [-1]
    