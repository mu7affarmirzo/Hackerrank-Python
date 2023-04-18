import csv

lines = list()

with open('accounts 123.csv', mode='r', encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            lines.append(row)
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if row[3] == 'NULL':
            print(f"ID: {row[0]} --- phone: {row[3]}")
        else:
            lines.append(row)

        line_count += 1
    print(f'Processed {line_count} lines.')

with open('acounts_123.csv', 'w', encoding="utf-8", newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines,)

