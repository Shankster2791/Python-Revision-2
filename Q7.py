#Generalize the above implementation of csv parser to support any delimiter and comments.

import csv

def parse_csv(): 
    with open('sample.csv', newline='') as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|')
        for row in reader:
            print(','.join(row))
            
parse_csv()
