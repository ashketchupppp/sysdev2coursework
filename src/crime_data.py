from modules.main import * 
import os

if os.name == "nt":
    #Windows file paths
    crime_data_folder = ".\\data\\Devon_and_Cornwall_crime_data_2019"
    postcodes_csv = ".\\data\\Devon_postcodes\\postcodes.csv"
else:
    #Unix based OS paths
    crime_data_folder = "data/Devon_and_Cornwall_crime_data_2019"
    postcodes_csv = "data/Devon_postcodes/postcodes.csv"

main(crime_data_folder, postcodes_csv)
