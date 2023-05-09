import pandas as pd
import numpy as np

#read csv
df_own = pd.read_csv("nba_data_own.csv", header = 0)
df_op = pd.read_csv("nba_data_op.csv", header = 0)

df = pd.merge(df_own, df_op, left_on='Row.names', right_on='Row.names')
df = df.sort_values(by=['Row.names'])

#pd df to csv
df.to_csv('nba_data.csv', index=False, header=True)