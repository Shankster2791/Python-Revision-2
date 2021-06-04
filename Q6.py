#6. Write a python function ‘parse_csv’ to parse csv (comma separated values) files.

import csv

def parse_csv(): 
    with open('sample.csv','rt') as f:
      data = csv.reader(f)
      for row in data:
            print(row)
            
parse_csv()
