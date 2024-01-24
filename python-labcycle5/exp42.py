import csv

with open('mytemp.csv','r') as file:
    reader = csv.reader(file)

for row in reader:
    print(row)
