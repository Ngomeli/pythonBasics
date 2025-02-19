#Dataframe from dictionary
dict_data ={
    'Name': ['Jane', 'John', 'Mike'],
    'Age': [30, 25, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

import pandas as pd

df = pd.DataFrame(dict_data)

#print dataframe

print(df)