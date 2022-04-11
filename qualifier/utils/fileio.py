# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def save_csv(csvpath, csvdata):
    """"Opens the file corresponding to the csvpath and writes the table it recieves in CSV format

    Args:
        csvpath (Path) : The file to open and write to
        csvdata : list of list. Iterates through the outer list and creates a list for each list element within
    Returns:

    """
    # open the file using the cvspath object in write mode
    with open(csvpath, 'w', newline='') as csvfile:
        #create csvwriter object
        csvwriter=csv.writer(csvfile)
        # loop through the list csvdata
        for this_loan in csvdata:
            # for each loan found write a row in the csv file
            csvwriter.writerow(this_loan)
    return

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data
