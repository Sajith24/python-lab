import csv

with open('departments1.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)

print("ID Department Name")

print("---------------------------------")

for col in data:
    print(col['department_id'], col['department_name'])
