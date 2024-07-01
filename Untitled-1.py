
import csv

l = 'data-juBjDEKS03Bds6wun-5kM.csv'
with open(l, 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        print(row)