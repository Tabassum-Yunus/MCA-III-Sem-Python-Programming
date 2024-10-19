import pandas as pd
import numpy as np

data = {
    'Name': ['Jerry', 'Denny', 'Cookie'],
    'Status': ['Expired', 'Alive', 'Alive']
}
df = pd.DataFrame(data)
# print(df)
df.index = [chr(i+65) for i in range(3)]
print(df)
print(df['Name'])



data1 = np.random.randint(1,10,(10,10))   # creating an array of 6x5
df1 = pd.DataFrame(data1)               # convert the array into dataframe
df1.index = ['R'+str(i) for i in range(10)]  # assign row indices
df1.columns = ['C'+str(i) for i in range(10)]    # assign column indices

print(df1)  # print the whole dataframe





# arr = np.random.randint(1,10,(10,15))
# df = pd.DataFrame(arr, ['R'+str(i) for i in range(1,11)], ['C'+str(i) for i in range(1,16)])
# print(df)