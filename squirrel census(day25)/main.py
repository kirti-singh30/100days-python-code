import pandas
# data = pandas.read_csv("day25/weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())

## get the columns data
# print(data["condition"]) # both are givin same output of column data line 16 & 17
# print(data.condition)

##get the row data
# print(data[data.day == "Monday"]) #both are given same ouput of row data line 20 & 21
# print(data[data["day"] == "Monday"])

##get the max temp day
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# print(monday.temp) # change a temp in fahrenheit

# fahrenheit = (monday.temp *9/5) +32
# print(fahrenheit)

# montemp = int(monday.temp)
# fahrenheit = (montemp *9/5) +32
# print(fahrenheit)

##create a dataframe from scratch
# data_dict = {
#     "student": ["Amy","Sheldon","Raj","Penny"],
#     "score": [76,85,78,56]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirell_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirell_count)
red_squirell_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirell_count)
black_squirell_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirell_count)

squirel_data_dict = {
    "fur_color": ["Gray","Cinnamon","Black"],
    "count": [2473,392,103]
}
data = pandas.DataFrame(squirel_data_dict)
print(data)
data.to_csv("squrel_count.csv")