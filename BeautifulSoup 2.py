Extract Tecx from tags
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='entry-content')
 
lines = s.find_all('p')
 
for line in lines:
    print(line.text)
    
-------------------------------------------------------
Remove tags from the content of the leftbsr
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Finding by id
s = soup.find('div', id= 'main')
 
# Getting the leftbar
leftbar = s.find('ul', class_='leftBarList')
 
# All the li under the above ul
lines = leftbar.find_all('li')
 
for line in lines:
    print(line.text)
-------------------------------------------------------
Extracting links
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# find all the anchor tags with "href"
for link in soup.find_all('a'):
    print(link.get('href'))
----------------------------------------
