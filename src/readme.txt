This is a guide to configuring and using your crime data report generator.

# Running the code

Make sure you have python installed on your system.
Run the following command whilst in the same directory as the crime_data.py file
"python crime_data.py"

# Configuration Settings

By default there are four configuration settings in the crime_data.py file.
You may change any of these values as they are the folders which the program
will look into to try and load the postcode and crime data.

 - data_folder (default = 'data')
   this is the folder name which will be used for the postcode and crime data. 

 - crime_data_folder (default = 'Devon_and_Cornwall_crime_data_2019')
   this is the folder name which will be used for the crime data itself.
   the program will search the whole directory tree for all .csv files and attempt
   to load them, it is important they all have the same headings.
   You may organise the .csv files in this folder however you like, they will all be found.

 - postcodes_folder (default = 'Devon_postcodes') 
   this is the folder name which will be used to hold the postcodes_file_name.

 - postcodes_file_name (default = 'postcodes.csv')
   this is the file name which the program will attempt to read from the postcodes_folder.
   there must only be one postcodes.csv file.

Default Directory Structure using example data provided.

+--data
|  +--Devon_postcodes
|  |  +--postcodes.csv
|  +--Devon_and_Cornwall_crime_data_2019
|  |  +--2019-01
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-02
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-03
|  |  |   +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-04
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-05
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-06
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-07
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-08
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-09
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-10
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-11
|  |  |  +--2019-01-devon-and-cornwall-street.csv
|  |  +--2019-12
|__|__|  +--2019-01-devon-and-cornwall-street.csv

# General Guide

1. Do not separate the 'crime_data.py' file from the modules directory.
   They must always be in the same folder.
