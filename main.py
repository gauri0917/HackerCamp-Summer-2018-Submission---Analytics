

import pandas as pd

df = pd.read_csv('./Deduplication Problem - Sample Dataset.csv')

import cl as cl

df['fn']=df['fn'].apply(cl.process1)
df['ln']=df['ln'].apply(cl.process2)

import unique as un
un.uniq(df)


import replacement as rp

#applying functions to columns
df['fn']=df['fn'].apply(rp.process3)
df['ln']=df['ln'].apply(rp.process4)

#remove duplicate values
df=df.drop_duplicates()

#save in ouput file
df.to_csv('output.csv')