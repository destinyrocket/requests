#Extract Title of the Page
import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# Getting the title tag
print(soup.title)
 
# Getting the name of the tag
print(soup.title.name)
 
# Getting the name of parent tag
print(soup.title.parent.name)
 
# use the child attribute to get
# the name of the child tag

#---------------------------------------------------
#finding element by class

import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
 
print(content)
#----------------------------------
#Finding element by ID

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
content = leftbar.find_all('li')
 
print(content)
#-----------------------------------------------------&&




