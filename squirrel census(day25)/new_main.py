# with open("day25/weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

import csv

with open("day25/weather_data.csv") as weather_file:
    data = csv.reader(weather_file)
    #header = next(data) # we can use this function for get rid of temp
    temperatures = []
    for row in data:
        if row[1] != "temp":
        #temp_row = row[1]
        #temperatures.append(int(temp_row))
            temperatures.append(int(row[1]))
    print(temperatures)