'''
Extracts all matrices from the MapBiomas website
Each matrix extracted in a separate CSV
Date: 10/24/2020
'''

from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Firefox(executable_path='geckodriver.exe')
url = 'https://plataforma.mapbiomas.org/'  # url for map
driver.get(url)
time.sleep(2)

# Close access box by clicking outside of it
body = driver.find_element_by_tag_name('body')
action = webdriver.common.action_chains.ActionChains(driver)
action.move_to_element_with_offset(body, 5, 5)
action.click()
action.perform()
time.sleep(2)

# Transition tab
driver.find_elements_by_tag_name('li')[1].click()
time.sleep(2)
# Statistics Button
driver.find_element_by_class_name('MuiButton-label-2002').click()
time.sleep(1)
# Matrix Tab
driver.find_elements_by_class_name('TabList_navListItem__1Scvk')[4].click()

## These column names were in portuguese so I assigned new ones below
# col_names=[]
# html_list = driver.find_element_by_class_name('DashboardDialogTransitionContent_tableWrapper__vqAtI')
# items = html_list.find_elements_by_tag_name("li")
# for item in items:
#     text = item.text
#     col_names.append(text)

# column names for matrices
col_names = ['Forest', 'NaturalNonForestFormation', 'Agriculture', 'NonVegetatedArea',
             'BodiesofWater', 'NotObserved', 'Total']

# For each year load matrix and write to csv
for y in range(2, 59):
    time.sleep(3)
    # Year Dropdown
    driver.find_element_by_xpath('//*[@id="root"]/div/header/div[3]/div/div[1]/div[4]').click()
    time.sleep(2)
    # Each year in dropdown
    x_path = '/html/body/div[2]/div[3]/ul/li[' + str(y) +']'
    year = driver.find_element_by_xpath(x_path)
    year_txt = year.text + '.csv'
    print(year_txt)
    # Loads matrix on the right
    year.click()
    time.sleep(2)

    # create an empty dataframe
    df = pd.DataFrame(columns=col_names)
    # locate matrix
    hoursTable = driver.find_elements_by_tag_name("tr")

    # extract data and fix format
    for row, i in zip(hoursTable, range(len(hoursTable))):
        if i != 0:
            data_row = (row.text).split(' ')
            each_row = [item.encode('utf-8') for item in data_row]
            each_row = [sub.replace('.','') for sub in each_row]
            each_row = [sub.replace(',', '.') for sub in each_row]
            each_row = [round(float(x)) for x in each_row]
            # since we skip the first row that has column names in portuguese
            index_name = col_names[i-1]
            df.loc[index_name] = each_row

    # drop Total columns- not needed for pontiPy
    df.drop('Total', axis=1, inplace=True)
    df.drop('Total', axis=0, inplace=True)
    # write to csv
    df.to_csv (year_txt, index = True, header=True, encoding='utf-8')
