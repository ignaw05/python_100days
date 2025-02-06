# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250204.csv")
#
# gray = data[data["Primary Fur Color"] == "Gray"]
# black = data[data["Primary Fur Color"] == "Black"]
# cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
#
# dict = {
#     "Fur Color" : ["Gray", "Black", "Cinnamon"],
#     "Count": [len(gray),len(black),len(cinnamon)]
# }
#
# dataf = pandas.DataFrame(dict)
# dataf.to_csv("ColorFur.csv")

import pandas
from turtle import Turtle