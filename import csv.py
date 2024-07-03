import csv
import os

data_files = ['data-juBjDEKS03Bds6wun-5kM.csv', 'data-mhC2yxsAXZTSCXLFsrPLU.csv', 'data-oBewWktMX5Z6JGaB-2V3z.csv', 'data-sm3_cxHiLqpa38sOpi7hk.csv','data-yzRZxpoxRgFCQr55Cc6kl.csv']
countries = [] 

people={}

def read_csv(file_name):
    print('============>', file_name)
    with open(file_name, 'r') as file:
        persons_in_the_csv_file = csv.reader(file)
        for person in persons_in_the_csv_file:
            country = person[1]
            region = person[2]
            secret = person[3]
            company = person[4]
            region1 = person[5]
            currency = person[6]
            fullname = person[0]
            # print(country)
            if not country in countries:
                countries.append(country)
                people[country] = []
            people[country].append(person)
            
            

fields = ['country', 'region','secret', 'company', 'region1', 'currency', 'fullname']

def write_csv(file_name):
    print("I'll write file named: ", file_name)

    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

for data_file in data_files:
    read_csv(data_file)


for country in countries:
    write_csv( os.path.join( 'data', country))

print(people)
