import pandas as pd
from pontiPy import *
import os
import glob
import numpy as np

os.chdir("../DATA/TRANSITION")

def biome_contingency(time_interval = 1):
    directories = glob.glob("*")
    # each biome subdirectory
    for dir in directories:
        # empty dataframe and lists
        _cat1, _cat2, _cat_exchange, _biome, _year = [], [], [], [], []
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
                # print (df)
                fname_csv = os.path.basename(file_name)
                fname_csv = fname_csv.replace('.csv', '')
                # list of all column indices
                column_index = list(range(0, len(df.columns)))
                # print(column_index)
                # compute all category combinations
                combinations = [(column_index[i], column_index[j]) for i in range(len(column_index)) for j in range(i + 1, len(column_index))]
                # print(combinations)
                # print(combinations[0][1])

                obj = pontiPy_Change(df)
                if time_interval == 5:
                    # compute exchange for each combination
                    for i in combinations:
                        # print (i, df.columns[i[0]],df.columns[i[1]])
                        _year.append(fname_csv)
                        _cat1.append(df.columns[i[0]])
                        _cat2.append(df.index[i[1]])
                        _cat_exchange.append(round(obj.exchange(i[0],i[1])))
                        print(fname_csv, df.columns[i[0]], df.index[i[1]], obj.exchange(i[0],i[1]))

                # combine lists into df
                plot_df = pd.DataFrame(
                    {'year':_year,
                    'category1': _cat1,
                     'category2': _cat2,
                     'exchange': _cat_exchange
                    })
                # rearrange columns
                plot_df = plot_df[['category1', 'category2', 'exchange']]
                # print(plot_df)
                # save to file
                # data_crosstab = plot_df.pivot_table(plot_df['category1'],
                #                             plot_df['category2'],
                #                             margins=False, aggfunc = {'exchange': np.sum})
                data_crosstab = pd.pivot_table(plot_df, index='category1', columns='category2', values='exchange', margins=False)


                print(data_crosstab)


                biome_name = '../EXCHANGE/' + dir + '_' + str(fname_csv) + '_ex' + '.csv'
                data_crosstab.to_csv(biome_name, index=True)

biome_contingency(5)