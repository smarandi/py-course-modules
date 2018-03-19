import csv

def problem3_7(csv_pricefile, flower):
    file = open(csv_pricefile)
    price = {}
    for row in csv.reader(file):
        if flower == row[0]:
            print(row[1])

# problem3_7("flowers.csv", "begonia")
