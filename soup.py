#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
import re
from datetime import datetime
import string
from colorama import Fore, Back, Style
from selenium import webdriver

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

def Separador():

    print("==================================================================================================================================\n")

def Sec():
    print("-----------------------------------------------------------------------------------------------------------------------------------\n")

def Nav(i):

    url = "http://ufm.edu/"
    url2 = url + i.text

    try:
        html_content = requests.get(url2).text
        print(f"Succes! Now you are in {url2}\n")
    except:
        print(f"unable to get {url}")
        sys.exit(1)

    souper = BeautifulSoup(html_content, "html.parser")

    return souper

def NavCS(url):

    try:
        html_content = requests.get(url).text
        print(f"Succes! Now you are in {url}\n")
    except:
        print(f"unable to get {url}")
        sys.exit(1)

    souper = BeautifulSoup(html_content, "html.parser")

    return souper


def Logfile():
    # ------------------------------------------ Log File --------------------------------------------------------------
    #Write a log file to store the output
    log_file = open("logs/logfile.txt", "w")

    for div in soup.find_all("a"):

        #This will save the data to the logfile
        sys.stdout = log_file

        print(div)
        Sec()

        sys.stdout = stdout

    log_file.close()

    print(currentDT.strftime(Fore.CYAN +"\nDate of generation: %a, %b %d, %Y, %I:%M:%S %p\n"))
    Separador()

def Portal():
    Separador()
    print('1. Portal\n')
    address = soup.find("a", {"href": "#myModal"})       #This is the Complete Address of UFM 
    phone = soup.find("a", {"href": "tel:+50223387700"})       #This is the phone 
    mail = soup.find("a", {"href": "mailto:inf@ufm.edu"})       #This is the info mail
    item = soup.find("table", {"id": "menu-table"})             #This is the items of the menu-table
    s = item.text
    h = " ".join(s.split())
    for link in soup.findAll('a', attrs={'href': re.compile("auto&hd=ufm.edu$")}): #for loop to get the href of UFMail button
        ufmbtn = link.get('href')
    for link in soup.findAll('a', attrs={'href': re.compile("ejemplo%40ufm.edu$")}): # for loop to get the href of MiU button
        miubtn = link.get('href')
    a = len(soup.findAll('a'))

    
    print(Fore.BLUE + 'Title: \n',Style.RESET_ALL, soup.title.string, '\n')         #This is the Title 
    print(Fore.BLUE + 'Address: \n', Style.RESET_ALL, address.text, '\n')
    print(Fore.BLUE +'Phone and info email: \n',Style.RESET_ALL, phone.text, '\n',mail.text, '\n')
    print(Fore.BLUE + 'Item of nav menu:', Style.RESET_ALL, h, '\n')
    print(Fore.BLUE +'Href of "UFMail" button: \n',Style.RESET_ALL,ufmbtn, '\n')
    print(Fore.BLUE + 'Href of "MiU" button: \n', Style.RESET_ALL, miubtn, '\n')
    print(Fore.BLUE + 'All properties that have href: \n')
    i=0
    for link in soup.find_all("a"):
        print(Fore.GREEN + 'href link: ', Style.RESET_ALL, link.get('href'))
        Sec()
        if(i==30):
            print(Fore.RED +"Output exceeds 30 lines, sending output to: logs/logfile.txt.")
            Logfile()
            break
        i+=1
    for img in soup.findAll('img'):
        
        print(Fore.GREEN + 'Image link: ', Style.RESET_ALL, img.get('src'))
        Sec()
    print(Fore.BLUE + 'All a in UFM webpage: \n', Style.RESET_ALL, a, '\n')

def Estudios():
    Separador()
    print('2. Estudios\n')
    #es = soup.find("a", {"href": "/Estudios"})
    es = "https://ufm.edu/Estudios"
    souper = NavCS(es)

    #This is the items of the top menu
    item = souper.find("div", {"id": "topmenu"})
    st = item.text
    l = " ".join(st.split())
    est = souper.find_all("div", {"class": "estudios"})
    lii = souper.find("div", {"class": "leftbar"}).find_all("li")
    sm = souper.find("div", {"class": "social pull-right"}).find_all("a")
    
    print(Fore.BLUE + 'Item of nav menu:', Style.RESET_ALL, l, '\n')
    Separador()
    for i in range(len(est)):
        print(Fore.BLUE + 'Estudios: \n',
              Style.RESET_ALL, est[i].get_text(), '\n')
        Sec()
    Separador()
    for i in range(len(lii)):
        print(Fore.BLUE + 'List items: \n',
              Style.RESET_ALL, lii[i].get_text(), '\n')
        Sec()
    Separador()
    for i in range(len(sm)):
        print(Fore.BLUE + 'Social Media: \n',
              Style.RESET_ALL, sm[i]['href'], '\n')
        Sec()

def CS():
    Separador()
    print('3. CS\n')
    u = "https://fce.ufm.edu/carrera/cs/"
    soupers = NavCS(u)
    acs = len(soupers.findAll('a'))
    divcs = len(soupers.findAll('div'))

    print(Fore.BLUE + 'Title Computer Science: \n', Style.RESET_ALL, soupers.title.string, '\n')
    print(Fore.BLUE + 'All a in CS webpage: \n', Style.RESET_ALL, acs, '\n')
    print(Fore.BLUE + 'All div in CS webpage: \n', Style.RESET_ALL, divcs, '\n')

def Directorio():
    print('\nThis is the Directorio function.\n')



print('\n<Fernando González>\n')

# ------------------------------------------------- Verificador de argumentos ------------------------------------------
if len(program) == 1:                               #Si solo pasa un argumento (el nombre del programa)
    Portal()
    Estudios()
    CS()
    #Directorio()
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


