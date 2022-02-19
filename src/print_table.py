
from readit import *
from facts import *
from tabulate import tabulate

def print_table (filename):
    """
    takes in a file, reads and processes it (for data files that follow .csv format)
    reports information about number of columns and rows (for any data file per row 14)
    and reports vaccination status (specific to vax status data file)
    """
    listofdicts = readit(filename)                                              
    list = facts(listofdicts)                                                     
    print("Your data has {0} columns and {1} rows.".format(list[0], list[1]))
    if list[0] < 100:
        print("\nAvailable fields:")
        table = []
        cols = 3
        i = 0
        while i <= len(list[2]):
            row = []
            for j in range (cols):
                if i+j <= len(list[2]):
                    try:
                      row.append(list[2][i+j])
                    except:
                      continue
                else:
                    break
            table.append(row)
            if i+cols < len(list[2]):
                i = i + cols
            else:
                break

        print(tabulate(table, tablefmt="plain"))

    else:
        print("Too many (> 100) fields available to print in table")
