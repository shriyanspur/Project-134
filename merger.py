import csv
import pandas as pd

dataset1 = []
dataset2 = []

file1 = 'list_of_stars.csv'
file2 = 'bright_stars.csv'

with open (file1, 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open (file2, 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

header1 = dataset1[0]
star_data1 = dataset1[1:]

header2 = dataset2[0]
star_data2 = dataset2[1:]

headers = header1+header2
star_data = []

for data1 in star_data1:
    star_data.append(data1)

for data2 in star_data2:
    star_data.append(data2)

with open('merged_data.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)