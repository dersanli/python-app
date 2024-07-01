import csv

data_file = 'data-juBjDEKS03Bds6wun-5kM.csv'


with open(data_file,'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        country = row[1]
        region = row[2]
        secret = row[3]
        company = row[4]
        region1 = row[5]
        currency = row[6]
        fullname = row[0]
        names = fullname.split(' ')
      
        if (len(names)==2):
            surname = names[1]
            print(surname, secret, currency)
        else:
            print(secret, currency)
     
        