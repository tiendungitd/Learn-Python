# with open("weather_data.csv","r") as weather_data:
#     print(weather_data.readlines())

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)
import pandas

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])
# print(data.to_dict())
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))
# # average by panda
# print(data["temp"].mean())
# Get row of data
# print(data[data.temp == 12])
#print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")