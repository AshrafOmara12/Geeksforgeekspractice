from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.geeksforgeeks.org/python-list/'
# url = 'https://www.geeksforgeeks.org/transparent-window-in-tkinter/'
url_link = requests.get(url)

file = BeautifulSoup(url_link.content,'html.parser')

Function_detail = []
links = []
all_data = []


for table in file.findAll('figure', class_='table'):
    for td in table.findAll('td'):
        Function_detail.append(td.text)
        all_data.append(td.a)

Function_Name = Function_detail[0::2]
Description = Function_detail[1::2]
# print(len(Function_detail[1::2]))

for i in all_data[0::2]:
    # print(i)
    if i != None:
        links.append(i['href'])
    else:
        links.append('No link')

# print(links)

data_dict = {'Function Name':Function_Name,'Function Description':Description,
             'Links':links}

df = pd.DataFrame(data_dict)

df.to_csv('final_all.csv', index=False)