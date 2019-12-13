import requests
from bs4 import BeautifulSoup

#Start a link to a target website
url = "https://azurlane.koumakan.jp/List_of_Ships";
response = requests.get(url);


#If checking if the website loaded properly if not close the script
if response.status_code != 200 : exit()

#Getting the html
soup = BeautifulSoup(response.content, 'html5lib');

#---------------------------------------------------------------

#Finding targeted data within the table using class tag
table = soup.find_all('table', class_ = 'wikitable sortable jquery-tablesorter')

#Separating the table with the same class tag
#Normal Ship    --> table[0]
#Priority Ship  --> table[1]
#Collab Ship    --> table[2]
#Retrofit Ship  --> table[3]

normalShip = table[0]
prShip = table[1]     
collabShip = table[2] 

#---------------------------------------------------------------
#Reading the content in the name column for each row and storing them
#---------------------------------------------------------------

nShip = []

for row in normalShip.find_all('tr'):
        i = 0
        for cell in row.find_all('td'):
            i += 1
            if i == 2:
                nShip.append(cell.text)
                i = 0
                break

#---------------------------------------------------------------

pShip = []

for row in prShip.find_all('tr'):
        i = 0
        for cell in row.find_all('td'):
            i += 1
            if i == 2:
                pShip.append(cell.text)
                i = 0
                break

#---------------------------------------------------------------

cShip = []

for row in collabShip.find_all('tr'):
        i = 0
        for cell in row.find_all('td'):
            i += 1
            if i == 2:
                nShip.append(cell.text)
                i = 0
                break

#---------------------------------------------------------------
#Saving the name to a file

with open('NormalShipList.txt', 'w') as r:
    for ship in nShip:
        r.write(ship + '\n')

with open('PriorityShipList.txt', 'w') as r:
    for ship in pShip:
        r.write(ship + '\n')

with open('CollabShipList.txt', 'w') as r:
    for ship in cShip:
        r.write(ship + '\n')

