import csv
import os

def csv_to_dict(filepath):
    """Reads a .csv file and outputs the contents into a list of dictionaries."""
    # ensure that the path exists
    if os.path.exists(filepath):
        with open(filepath, newline='') as csvfile:
            # use built in csv reader to read csv file
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
    # note that the heading order will be preserved as python dictionaries
    # store the data in the order it was put in