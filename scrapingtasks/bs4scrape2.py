from csv import writer
from dataclasses import field
import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.passiton.com/inspirational-quotes"
r = requests.get(url)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
table = soup.find('div', attrs={'id': 'all_quotes'})
# print(table)

qoutes = []
for row in table.findAll('div',attrs={'class': 'col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top'}):
    # print(row)
    qoute = { }
    qoute['theme'] = row.h5.text
    qoute['url'] = row.a['href']
    qoute['image'] = row.img['src']
    qoute['lines'] = row.img['alt'].split('.')[0]

    qoutes.append(qoute)

# print("\n",qoutes[0]['theme'],"\n",qoutes[0]['url'],"\n",qoutes[0]['image'],"\n",qoutes[0]['lines'])
# print(qoutes)
with open('qoutes.csv','w') as f:
    fieldnames = ['theme', 'url', 'image', 'lines']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for qoute in qoutes:
        writer.writerow(qoute)

    
    
    
