from modules.main import * 
import os

# change these values to change the folders and files
# the program will use to load the postcode and crime data from

data_folder = 'data'
crime_data_folder = 'Devon_and_Cornwall_crime_data_2019'
postcodes_folder = 'Devon_postcodes'
postcodes_file_name = 'postcodes.csv'

# +--<data_folder>
# |  +--<postcodes_folder>
# |  |  +--<postcodes_file_name>
# |  +--<crime_data_folder>

# setup the directories
crime_data_folder = '{}/{}'.format(data_folder, crime_data_folder)
postcodes_csv = '{}/{}/{}'.format(data_folder, postcodes_folder, postcodes_file_name)

# call main
main(crime_data_folder, postcodes_csv)
