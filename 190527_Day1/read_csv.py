with open('lunch_join.csv', 'r', encoding='utf-8') as f :
    lines = f.readlines()
    for line in lines:
        print(len(line))
        print(len(line.strip()))
        print(line.strip().split(','))

import csv
with open('lunch_join.csv', 'r', encoding='utf-8') as f :
    items = csv.reader(f)
    for item in items:
        print(item)