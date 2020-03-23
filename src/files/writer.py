from fileutil import *
def dict_to_csv(filepath, content):
    """Writes contents of a dictionary list to csv format"""
    #Checking content type, retun if invalid
    if not isinstance(content,(list,dict)):
        print("Not List or Dictionary")
        return [-1]
    if content == "":
        print("Content empty")
        return [-1]
    #Create list of keys, for headings
    keys = content[0].keys()
    if keys == "":
        print("Empty keys")
        return [-1]
    writer = write_csv(filepath, content, keys)
    return writer