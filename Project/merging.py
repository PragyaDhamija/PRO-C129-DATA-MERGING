import csv

dataset_1 = []
dataset_2 = []

with open("dataset_1.csv" , "r") as f:
    c1 = csv.reader(f)
    for row in c1:
        dataset_1.append(row)

with open("dataset_2.csv" , "r") as i:
    c2 = csv.reader(i)
    for row in c2:
        dataset_2.append(row)

headers_1 = dataset_1[0]
planet_data_1 = dataset_1[1:]

headers_2 = dataset_2[0]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2 
planet_data = []
for index , data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])    

with open("final.csv" , "a+") as k:
    c = csv.writer(k)
    c.writerow(headers)
    c.writerows(planet_data)