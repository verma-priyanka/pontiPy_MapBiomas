import pandas as pd
from pontiPy import *
import os
import glob

os.chdir("../DATA/TRANSITION")

def biome_contingency(time_interval = 1):
    directories = glob.glob("*")
    # each biome subdirectory
    for dir in directories:
        # empty dataframe and lists
        _year, _category = [], []
        _quantity, _exchange, _shift  = [], [], []
        df = pd.DataFrame(None)
        # get all csvs for biome
        d = dir + '/*.csv'
        for file_name in glob.iglob(d, recursive=True):
            # extract yearly or 5 year csvs based on function parameter
            csv_file = str(file_name).split("\\")
            file_split = str(csv_file[1]).replace('.csv', '')
            file_split = file_split.split(' to ')
            if int(file_split[1]) - int(file_split[0]) == time_interval:
                df = pd.read_csv(file_name, index_col=0)
                # replace nan with 0
                df = df.fillna(0)
                fname_csv = os.path.basename(file_name)
                fname_csv = fname_csv.replace('.csv', '')

                obj = pontiPy_Change(df)
                if time_interval == 1:
                    for col in range(len(df.columns)):
                        _category.append(df.columns[col])
                        _year.append(fname_csv)
                        _quantity.append(round(obj.quantity(col)))
                        _exchange.append(round(obj.exchange(col, Total = True)))
                        _shift.append(round(obj.shift(col)))
                else:
                    for col in range(len(df.columns)):
                        _category.append(df.columns[col])
                        _year.append(fname_csv)
                        _quantity.append(round(obj.quantity(col)/time_interval))
                        _exchange.append(round(obj.exchange(col, Total = True)/time_interval))
                        _shift.append(round(obj.shift(col)/time_interval))

            # combine lists into df
            plot_df = pd.DataFrame(
                {'Year': _year,
                 'Category': _category,
                 'Quantity': _quantity,
                 'Exchange': _exchange,
                 'Shift': _shift
                })
            # rearrange columns
            plot_df = plot_df[['Year', 'Category', 'Quantity', 'Exchange', 'Shift']]
            # save to file
            biome_name = '../BIOME_CONTINGENCY/CATEGORY/' + dir + '_' + str(time_interval) + 'year' + '.csv'
            plot_df.to_csv(biome_name)

biome_contingency(1)