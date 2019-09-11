#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

# This will get the number of function the user will send as an input
program = sys.argv

url="http://ufm.edu/Portal"

# Make a GET request to fetch the raw HTML content

try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())


def Portal():
    print('1. Portal\n')
    address = soup.find("a", {"href": "#myModal"})       #This is the Complete Address of UFM 
    phone = soup.find("a", {"href": "tel:+50223387700"})       #This is the phone 
    mail = soup.find("a", {"href": "mailto:inf@ufm.edu"})       #This is the info mail
    #print('\nThis is the title with HTML objects: \n', soup.title, '\n')
    print('Title: \n', soup.title.string, '\n')         #This is the Title 
    print('Address: \n',address.text, '\n')
    print('Phone and info email: \n', phone.text, '\n',mail.text, '\n')

print('\n<Fernando González>\n')

# ------------------------------------------------- Verificador de argumentos ------------------------------------------
if len(program) == 1:                               #Si solo pasa un argumento (el nombre del programa)
    print('En teoria se corre todo el código.')
elif program[1] == 1 or program[1] =='1':           #Si manda 1, entonces se va a la funcion del protal
    Portal()

'''
for div in soup.find_all("div"):
    print(div)
    print("--------------------------")

'''
