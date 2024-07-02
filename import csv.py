import csv

data_files = ['data-juBjDEKS03Bds6wun-5kM.csv','data-mhC2yxsAXZTSCXLFsrPLU.csv','data-oBewWktMX5Z6JGaB-2V3z.csv','data-sm3_cxHiLqpa38sOpi7hk.csv', 'data-yzRZxpoxRgFCQr55Cc6kl.csv']



def read_csv(file_name):
    print('============>',file_name)
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            print(row)


for data_file in data_files:
    read_csv(data_file)
  




# with fileinput.input files ='data_file1', 'data_file2', 'data_file3', 'data_file4', 'data_file5') as f:
#     for line in f:
#         print(line)
