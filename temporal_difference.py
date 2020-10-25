# import pontiPy
import pandas as pd
from pontiPy import *

# import glob
import glob

# create empty lists
q = []
e = []
s = []

# define path for folder
path = "DATA/YEARLY/*.csv"

# loop through csv
for fname in glob.glob(path):
    df = pd.read_csv(fname, index_col=0)
    obj = pontiPy_Change(df)

    q_value = round(obj.quantity())
    e_value = round(obj.exchange())
    s_value = round(obj.shift())

    q.append(q_value)
    e.append(e_value)
    s.append(s_value)

# combine lists into df
plot_df = pd.DataFrame(
    {'Quantity': q,
     'Exchange': e,
     'Shift': s
    })

print(plot_df)