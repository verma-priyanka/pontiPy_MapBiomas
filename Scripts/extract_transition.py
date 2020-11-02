"""
Creates directory for each biome (Level-2 Data)
Generates confusion matrices by biome for every 1-year and 5-year intervals
Date: 11/01/2020
"""
import pandas as pd
import numpy as np
from pontiPy import *
import os

os.chdir("../DATA/TRANSITION/")
file = "Transicao_MapBiomas_level2.csv"
df = pd.read_csv(file)

# extract unique biome names
biomes = df.biome.unique()
for biome in df.biome.unique():
    print("Creating Matrices for: ",biome)
    # directory for each biome
    os.mkdir(biome)
    # generate confusion matrix for every year
    for year in df.columns[6:]:
        df_biome_filter = df[df['biome']== biome]
        # pivot data
        lvl2_transition = df_biome_filter.pivot_table(index='from_level_2', columns='to_level_2', values=year, aggfunc=np.sum)
        # remove name from first col/row
        lvl2_transition = lvl2_transition.rename_axis(None, axis = 1)
        lvl2_transition = lvl2_transition.rename_axis(None, axis = 0)
        # save to csv
        filename = year +'.csv'
        lvl2_transition.to_csv(os.path.join(biome, filename))