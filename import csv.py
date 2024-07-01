import csv

data_file = 'data-juBjDEKS03Bds6wun-5kM.csv'

with open(data_file,'r') as file:
    csvreader = csv.reader(file)
    
    for row in csvreader:
        country = row [1]
        currency = row [6]
        fullname = row [0]
        names = fullname.split(' ')

        
        if (len(names)==2):
            surname = names[1]
            print(surname, country, currency)
        else:
            print(country,currency)
