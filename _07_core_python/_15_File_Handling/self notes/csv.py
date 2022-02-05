import csv

with open('family.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The Column names are as follows {",".join(row)}')
            line_count += 1
        print(f'\ti am {row["name"]} and my age {row["age"]}  and my occupation is {row["occupation"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
