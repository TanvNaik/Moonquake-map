import json
import csv

with open ('newdata.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    next(reader)
    data = []
    for row in reader:

        lst = row[0].split('|')
        print(lst)

        data.append({
            "lat": lst[4],
            "lng": lst[5],
            "year": lst[-1].split("T")[0].split('-')[0],
            "date": lst[-1].split("T")[0],
            "startTime": lst[-2].split("T")[0] + " " + lst[-2].split("T")[1],
            "endTime": lst[-1].split("T")[0] + " " + lst[-1].split("T")[1],
        })

with open('./moonquakes.json', 'w') as f:
    json.dump(data, f, indent=4)
