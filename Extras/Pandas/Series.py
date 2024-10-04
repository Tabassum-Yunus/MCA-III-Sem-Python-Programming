''' Creating Series object os pandas and giving index to them   '''

import pandas as pd
a = ['Google', 'Colab', 'GMeet', 'Drive']
series = pd.Series(a)
# Series with default indices i.e., 0,1,2,3---
print(series)

# Series with defined indices i.e., a,b,c,d---
series.index = ['a','b', 'c','d']       # if indices are less than elements ---> will give error
print(series)