import csv

data = []

with open("dataset_2.csv", "r") as k:
    c = csv.reader(k)
    for a in c: 
        data.append(a)

header = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[2] = data_point[2].lower()

planet_data.sort(key=lambda planet_data: planet_data[2])


with open("dataset_2_sorted.csv", "a+") as v:
    c = csv.writer(v)
    c.writerow(header)
    c.writerows(planet_data)