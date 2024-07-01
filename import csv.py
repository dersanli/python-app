import csv

def load_data(filename):
    mylist = []
    with open(filename) as info:
        info_data = csv.reader(info, delimiter=',')
        next(info_data) 
        for row in info_data:
            mylist.append(row)
        return mylist
    
newlist = load_data('data-juBjDEKS03Bds6wun-5kM.csv')
for row in newlist:
    print(row)