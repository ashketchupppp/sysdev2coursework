def search_list_dict(postcodes, search, key):
    """
    Searches a list of dictionaries
    Three variables: a list of dictionaries, search value and key to search
    Return array containing -1 if not found, and -2 if multiple results found
    """
    result = []
    count = 0
    #Make sure the key exists in dictionary, return  [-1] if not
    try:
        keyerror = postcodes[0][key]
    except:
        return [-1]
    #loop over list set result to last matching item
    for i in postcodes:
        if (i[key] == search):
            count += 1
            result = i
    #retunr -1 if no results found
    if result == []:
        result = [-1]
    #Return -2 if more than one result found
    if count > 1:
        result = [-2]
    return result



