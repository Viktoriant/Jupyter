import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_daily.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

lst = soup.find_all('name')

for item in lst:
    print(item)

url = "https://matplotlib.org/stablibe/gallery/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)


lst = soup.find_all('h2')

for item in lst:
    print(item)

def clean_item(my_item):
    position = my_item.find('<a')
    return my_item[4:position]

print()

for item in lst:
    print(clean_item(str(item)))
          
lst = soup.find_all(class_='std std-ref')


for item in lst:
    print(item)

def clean_item2(my_item):
    position = my_item.find('</')
    return my_item[26:position]

print()

for item in lst:
    print(clean_item2(str(item)))
          







