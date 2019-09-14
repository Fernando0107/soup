#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import re
from datetime import date
from datetime import datetime


# This will get the number of function the user will send as an input
program = sys.argv
stdout = sys.stdout
currentDT = datetime.now()

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

def Logfile():
    # ------------------------------------------ Log File --------------------------------------------------------------
    #Write a log file to store the output
    log_file = open("logs/logfile.txt", "w")

    for div in soup.find_all("a"):

        #This will save the data to the logfile
        sys.stdout = log_file

        print(div)
        print("==================================================================================================================================\n")

        sys.stdout = stdout

        #log_file.close()

    print(currentDT.strftime("\nDate of generation: %a, %b %d, %Y, %I:%M:%S %p\n"))


def Portal():
    print('1. Portal\n')
    address = soup.find("a", {"href": "#myModal"})       #This is the Complete Address of UFM 
    phone = soup.find("a", {"href": "tel:+50223387700"})       #This is the phone 
    mail = soup.find("a", {"href": "mailto:inf@ufm.edu"})       #This is the info mail
    item = soup.find("table", {"id": "menu-table"})             #This is the items of the menu-table
    for link in soup.findAll('a', attrs={'href': re.compile("auto&hd=ufm.edu$")}): #for loop to get the href of UFMail button
        ufmbtn = link.get('href')
    for link in soup.findAll('a', attrs={'href': re.compile("ejemplo%40ufm.edu$")}): # for loop to get the href of MiU button
        miubtn = link.get('href')
    
    print('Title: \n', soup.title.string, '\n')         #This is the Title 
    print('Address: \n',address.text, '\n')
    print('Phone and info email: \n', phone.text, '\n',mail.text, '\n')
    #print('Item of nav menu:',item.text, '\n')
    print('Href of "UFMail" button: \n',ufmbtn, '\n')
    print('Href of "MiU" button: \n', miubtn, '\n')
    print('All properties that have href: \n')
    i=0
    for link in soup.find_all("a"):
        print('href link: ', link.get('href'))
        print("==================================================================================================================================\n")
        if(i==30):
            print("Output exceeds 30 lines, sending output to: logs/logfile.txt.")
            Logfile()
            break
        i+=1

def Estudios():
    print('\nThis is the Estudios function.\n')

def CS():
    print('\nThis is the CS function.\n')

def Directorio():
    print('\nThis is the Directorio function.\n')



print('\n<Fernando González>\n')

# ------------------------------------------------- Verificador de argumentos ------------------------------------------
if len(program) == 1:                               #Si solo pasa un argumento (el nombre del programa)
    Portal()
    Estudios()
    CS()
    Directorio()
elif program[1] == 1 or program[1] =='1':           #Si manda 1, entonces se va a la funcion del protal
    Portal()
elif program[1] == 2 or program[1] =='2':           #Si manda 2, entonces se va a la funcion de Estudios
    Estudios()
elif program[1] == 3 or program[1] == '3':          #Si manda 3, entonces se va a la funcion de CS
    CS()
elif program[1] == 4 or program[1] == '4':          #Si manda 4, entonces se va a la funcion de Directorio
    Directorio()
else:
    print('\nError! You need to send a valid argument.\n')
