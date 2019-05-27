lunch = {
    '양자강': '02-557-4211',
    '감밥카페': '02-553-3181',
    '순남시레기':  '02-588-0887'
}

for k, v in lunch.items():
    print(k, v)

#1. f-string
with open('lunch_fString.csv', 'w', encoding = 'utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')

#2. Join : str.join(item) : tuple/list형의 데이터들 사이를 ,로 구분하고 하나의 string으로 만든다.
with open('lunch_join.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(','.join(item) + '\n')

#3. csv
import csv
with open('lunch_csv.csv', 'w', encoding='UTF-8', newline='') as f :
    csv_writer = csv.writer(f)
    for item in lunch.items():
        print(item)
        csv_writer.writerow(item)
