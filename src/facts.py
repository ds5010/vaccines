def facts(listofdicts):
    """
    Read in a file name and report back # of columns, # of rows
    """
    factlist = []
    headers = list(listofdicts[0])
    factlist.append(len(headers)) # number of columns at index 0
    factlist.append(len(listofdicts)) # number of rows at index 1
    factlist.append(headers) # list of column names at index 2
    factlist.append(listofdicts[0]) # dictionary representing first row of data at index 3

    return factlist
