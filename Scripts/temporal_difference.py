import pandas as pd
from pontiPy import *
import os
import glob

# create empty lists
q, e, s, y = [], [], [], []

# define path for folder
path = "DATA/YEARLY/*.csv"
# path = "DATA/5_YEAR/*.csv"

# loop through csv
for fname in glob.glob(path):
    df = pd.read_csv(fname, index_col=0)
    fname_csv = os.path.basename(fname)
    fname_csv = fname_csv.replace(' a ',' to ')
    fname_csv = fname_csv.replace('.csv', '')
    # print(fname_csv)
    obj = pontiPy_Change(df)

    q_value = round(obj.quantity())
    e_value = round(obj.exchange())
    s_value = round(obj.shift())

    y.append(fname_csv)
    q.append(q_value)
    e.append(e_value)
    s.append(s_value)

# combine lists into df
plot_df = pd.DataFrame(
    {'Year':y,
     'Quantity': q,
     'Exchange': e,
     'Shift': s
    })
# rearrange columns
plot_df = plot_df[['Year', 'Quantity', 'Exchange', 'Shift']]
print(plot_df)

# save to file
# plot_df.to_csv('DATA/final_5YR.csv')
# plot_df.to_csv('DATA/final_Year.csv')