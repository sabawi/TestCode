import matplotlib.pyplot as plt
import scipy
import math as mat
import time as time
import numpy as np
import pandas as pd
import seaborn as sn 
import array as arr
import random as rand

Max =8
histo_max = 100
num_max = 51
number_of_draws = 0

histo = arr.array('i',(0 for i in range(0,num_max)))
print("array count = ",len(histo))

for k in range(1,histo_max+1):
    for i in range(1,Max+1):
        r = rand.randint(1,50)
        number_of_draws+=1
        histo[r]+=1

nparr= np.asarray(histo)
inx = np.array(range(0,51))
df = df_sorted = pd.DataFrame()

print("Number of Draws : ",number_of_draws)

df['Number'] = inx
df['Occurances'] = nparr
df['Percent'] = 100 * df['Occurances']/number_of_draws

df = df.drop([0])
df_sorted = df.copy()
df_sorted = df_sorted.sort_values(by=['Percent'], ascending=False)
print(df_sorted.to_string(index=False))

df['Percent'].plot.bar()
#
plt.show()