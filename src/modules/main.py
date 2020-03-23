from modules.commands import *

def main(full_path_to_crime_data_folder, full_path_to_devon_postcodes):
    help_message = """The following is a list of valid inputs:

    Help - display this message
    Quit - exit the program
    Retrieve - retrieve crime data
    Sort - sort retrieved crime data
    Filter - filter retrieved crime data
    Search - search retrieved crime data
    Save - save retrieved crime data to a file
    """
    welcome_message = "Welcome to the Crime Data search tool"

    end_program = False

    print("\n" + welcome_message)
    print(help_message)

    current_data = []

    while not end_program:
        user_input = input(" > ")
        user_input = user_input.lower()
        print()

        if user_input == "help":
            print(help_message) 

        elif user_input == "quit":
            end_program = True

        elif user_input == "retrieve":
            # this should return the crime data as a list of dictionaries
            # and assign what is passed back to a variable
            current_data = retrieve_crime_data()

        elif user_input == "sort":
            sort_crime_data()

        elif user_input == "filter":
            filter_crime_data()

        elif user_input == "search":
            search_crime_data()

        elif user_input == "save":
            save_crime_data()

        else:
            print("That is not a valid command. Type 'help' for a list of command.")
