import csv
import os

def csv_to_dict(filepath):
    """Reads a .csv file and outputs the contents into a dictionary."""
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
                    newRow[key] = row[key]
                # add the new row to the array
                outputArray.append(newRow)
        return outputArray
    else:
        return [-1]
