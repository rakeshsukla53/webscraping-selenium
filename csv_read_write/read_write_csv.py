import csv

with open('data1.csv', 'r+') as data_file:
    data = csv.DictReader(data_file)
    for row in data:
        print(row)

with open('data1.csv', 'r+') as data_file:
    data = csv.reader(data_file, delimiter='|')
    for row in data:
        print(row)

data = [
    ('japanese', '5', '2001'),
    ('korean', '2', '1998'),
    ('german', '4', '2005'),
    ('english', '10', '1990'),
    ('tamil', '7', '2010'),
]

headers = ('language', 'ability', 'started')

with open('write_data_1.csv', 'w+') as data_file:
    writer = csv.writer(data_file)
    writer.writerow(headers)
    writer.writerows(data)

data = [
    {'language': 'japanese', 'ability': '5', 'started': '2001'},
    {'language': 'korean', 'ability': '2', 'started': '1998'},
    {'language': 'german', 'ability': '4', 'started': '2005'},
    {'language': 'english', 'ability': '10', 'started': '1990'},
    {'language':'tamil', 'ability': '7', 'started':  '2010'}
]

with open('write_data_2.csv', 'w+') as data_file:
    writer = csv.DictWriter(data_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

