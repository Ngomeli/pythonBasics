#Dataframe from dictionary
"""dict_data ={
    'Name': ['Jane', 'John', 'Mike'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

import pandas as pd

df = pd.DataFrame(dict_data)

#print dataframe

print(df)"""
#Dataframe from list of dictionaries
names = ["United States", "Australia", "Japan", "Canada", "Italy", "Brazil"]
dr=[True, False, False, False, False, False]
cpc= [809,731,588,180,200,700]

import pandas as pd
#create dictonary my_dict with three keys:Value pairs:my_dict

my_dict = {"country":names, "drives_right":dr, "cars_per_cap":cpc}
#Build a DataFrame cars from my_dict: cars

cars = pd.DataFrame(my_dict)

#Defination of rows_labels
row_labels =["US", "AUS", "JPN", "CAN", "ITA", "BRA"]
#Specify row labels of cars

cars.index = row_labels
#print dataframe
#print(cars.loc["AUS"])
print(cars.iloc[2])