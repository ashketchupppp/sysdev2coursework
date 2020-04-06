from modules.fileutil import fileutil 
from modules.fileread import reader
from modules.ui.cli import InteractiveCommandLine
from modules.data.search import search_list_dict
from modules.commands import CmdRetrieveCrimeData

def load_crimedata(full_path_to_crime_data_folder):
    # search the provided folder for crime data
    crime_data_csv_files = fileutil.find_files(full_path_to_crime_data_folder, "csv")
    for num in range(len(crime_data_csv_files)):
        crime_data_csv_files[num] = crime_data_csv_files[num][0]
    crime_data = []
    # load all of the data from the csv files and put them in one list
    for csvfile in crime_data_csv_files:
        crime_data = crime_data + reader.csv_to_dict(csvfile)
    return crime_data
    
def load_postcodeData(full_path_to_devon_postcodes):
    # load the postcode data from the path given
    postcodes = reader.csv_to_dict(full_path_to_devon_postcodes)
    return postcodes
    
def main(full_path_to_crime_data_folder, full_path_to_devon_postcodes):
    # create the command line
    cmdLine = InteractiveCommandLine()
    
    # add the crime and postcode data
    cmdLine.addData('crimedata', load_crimedata(full_path_to_crime_data_folder))
    cmdLine.addData('postcodes', load_postcodeData(full_path_to_devon_postcodes))
    
    # set the welcome message
    cmdLine.setWelcome("Welcome to the Crime Data search tool")
    
    # add the CmdRetrieveCrimeData command to the command line
    cmdLine.addCommand(CmdRetrieveCrimeData(cmdLine))
    
    # start the command line
    cmdLine.run()