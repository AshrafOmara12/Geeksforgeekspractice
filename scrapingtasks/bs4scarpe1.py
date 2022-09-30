from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.geeksforgeeks.org/python-list/'
# url = 'https://www.geeksforgeeks.org/transparent-window-in-tkinter/'
url_link = requests.get(url)

file = BeautifulSoup(url_link.content,'html.parser')

table = file.find('figure', class_='table')
# header = table.find('tr')

# headers = []
#
# for row in header:
#     headers.append(row.text)

table_data = table.findAll('td')
Function_Name = []
Description = []
links = []
for td in table_data:
    if td.a != None:
        Function_Name.append(td.a.text)
        links.append(td.a['href'].strip())
    else:

        Description.append(td.text)

# df = pd.DataFrame(links)
# print(df)
# columns = ['Function Name', 'Function Description','Links']
# d
# print(df_1)
data_dict = {'Function Name':Function_Name,'Function Description':Description,
             'Links':links}

df = pd.DataFrame(data_dict)

df.to_csv('final', index=False)