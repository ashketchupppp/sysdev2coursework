import csv, sys
def find_coords(postcode):
    #read csv, and split on "," the line
    csv_file = csv.reader(open('postcodes.csv', "rt"), delimiter=",")

    #loop through csv list
    for row in csv_file:
        #if current rows postcode (1st) value is equal to input, print that row
        if postcode == row[0]:
             print(row)
             lat1 = float(row[10])
             lon1 = float(row[11])
             return lat1, lon1
