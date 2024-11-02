'''     Which crop needs highest average rainfall'''


import pandas as pd
df = pd.read_csv('Crop_recommendation.csv')
print(df)

print(df.groupby('label').mean()['rainfall'])   # print the mean rainfall of each crop

dict = df.groupby('label').mean()['rainfall']   # groupby() returns a dictionary
print(dict.max())                               # print the max mean value among each crop NOT THE LABEL(CROP NAME)



# m = 0
# for i in range(len(dict)):
#   if dict.iloc[i] > m:
#     m = dict.iloc[i]
#     k = dict.index[i]
# print('Crop:', k)
# print('Mean: ',m)


m = 0                               # bcz groupby() has returned a dictionary
for i,j in dict.items():
  if(j > m):
    m = j
    k = i
print('Crop:', k)
print('Mean: ',m)


# dict = df.groupby('label').mean()
# for i, j in dict.iterrows():
#   if j['rainfall'] == dict['rainfall'].max();
#     print(i)

