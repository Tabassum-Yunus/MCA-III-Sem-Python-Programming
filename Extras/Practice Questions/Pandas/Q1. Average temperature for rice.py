'''     Average temperature of the farms where rice are grown       '''

import pandas as pd
df = pd.read_csv('Crop_recommendation.csv')
print(df.tail())

print(df.info())

print(df.describe())

#print(df.groupby('label').mean())
df_a = df.groupby('label').mean()   # Calculates the mean of all features of each crop
print(df_a.loc['rice'])             # Calculates the mean of all features of rice

print(df.groupby('label').mean()['temperature'])    # Calculates the mean of temperature of each crop
df_g = df.groupby('label').mean()['temperature']

print(df_g.loc['rice'])   # Gives the avg temperature of rice


# df_g = df.groupby('label').mean()

# print(df_g['temperature'].loc['rice'])  