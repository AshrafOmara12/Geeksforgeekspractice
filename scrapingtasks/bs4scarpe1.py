import bs4 as bs
import requests

url = 'https://www.geeksforgeeks.org/python-list/'
url_link = requests.get(url)

# print(url_link.text)
file = bs.BeautifulSoup(url_link.text,'lxml')
# print(f
find_table = file.find("figure", {"class": "table"})

description = []
functions = []
links = []

for td in find_table.find_all('td'):
    print(td.a.text)


