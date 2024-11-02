'''     What is the range of humidity   '''

import pandas as pd
df = pd.read_csv('Crop_recommendation.csv')
print(df)

mn = df['humidity'].min()
mx = df['humidity'].max()
print('Range: ', mn, '-', mx)

