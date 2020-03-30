from modules.fileutil import fileutil 
from modules.csv import reader
from modules.ui.ui import *
from modules.data.search import search_list_dict
import modules.commands as commands

def main(full_path_to_crime_data_folder, full_path_to_devon_postcodes):
    help_message = """The following is a list of valid inputs:

    help - display this message
    quit - exit the program
    retrieve - retrieve and save to csv: all crime data within co-ordinate radius
    getcoord - retrieve and display: the latitude and longitude of an EX postcode
    """
    welcome_message = "Welcome to the Crime Data search tool"

    end_program = False

    # load the data from the paths given
    current_data = {} 
    current_data["postcodes"] = reader.csv_to_dict(full_path_to_devon_postcodes) 

    # search the provided folder for crime data
    crime_data_csv_files = fileutil.recursive_search(full_path_to_crime_data_folder, "*.csv")
    current_data["crimedata"] = []

    # load all of the data from the csv files
    for csvfile in crime_data_csv_files:
        current_data["crimedata"] = current_data["crimedata"] + reader.csv_to_dict(csvfile)

    print("\n" + welcome_message)
    print(help_message)


    while not end_program:
        user_input = input(" > ")
        user_input = user_input.lower()
        print()

        if user_input == "help":
            print(help_message) 

        elif user_input == "quit":
            end_program = True
    
        elif user_input == "retrieve":
            commands.retrieve_crime_data(current_data["postcodes"])

        elif user_input == "getcoord":
            commands.find_postcode_coordinate(current_data["postcodes"])

        else:
            print("That is not a valid command. Type 'help' for a list of command.")

