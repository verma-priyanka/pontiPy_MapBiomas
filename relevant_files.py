'''
Copies yearly matrices into a new directory for analysis
Date: 10/24/2020
'''
import os
import shutil

os.chdir(r'DATA')

for file in os.listdir("ALL"):
    source = r'ALL'
    target = ''
    if file.endswith(".csv"):
        file_split = str(file).replace('.csv', '')
        file_split = file_split.split(' a ')
        print(file_split[0], file_split[1])
        source = os.path.join(source, file)
        target = os.path.join(r'YEARLY')
        # check if yearly
        if int(file_split[1]) - int(file_split[0]) == 1:
            # copy
            shutil.copy(source, target)