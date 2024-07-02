import csv

data_files = ['data-juBjDEKS03Bds6wun-5kM.csv', 'data-mhC2yxsAXZTSCXLFsrPLU.csv', 'data-oBewWktMX5Z6JGaB-2V3z.csv', 'data-sm3_cxHiLqpa38sOpi7hk.csv','data-yzRZxpoxRgFCQr55Cc6kl.csv']
countries = [] 

def read_csv(file_name):
    print('============>', file_name)
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            country = row[1]
            region = row[2]
            secret = row[3]
            company = row[4]
            region1 = row[5]
            currency = row[6]
            fullname = row[0]
            # print(country)
            if not country in countries:
                countries.append(country)

fields = ['country', 'region','secret', 'company', 'region1', 'currency', 'fullname']

def write_csv(file_name):
    print("I'll write file named: ", file_name)
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()


for data_file in data_files:
    read_csv(data_file)

for country in countries:
    write_csv(country)
    
# print(countries)

