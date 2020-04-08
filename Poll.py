import VotingService

import os
import csv

# set csv file path for data
poll_csv = os.path.join('election_data.txt')

#read in the CSV file
with open(poll_csv, newline= '\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = 't')

    #adjust for header
    csv_header = next(csvfile)

    #use function
    VotingService.get_results(csvreader)

