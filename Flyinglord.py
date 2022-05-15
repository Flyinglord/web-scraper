from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.sportsbettingstats.com/nba/odds"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

#equipos

team = soup.find_all("div", class_="first teams type")

equipos = list()

count = 0
for i in team:
    if count < 1:
      equipos.append(i.text)
    else:
        break
    count += 1


#odds

prob = soup.find_all("div", class_="book spread book 1")

odds = list()

count = 0
for i in prob:
    if count < 1:
      odds.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({'Nombre': equipos, 'Probabilidad a favor': odds}, index=list(range(1, 2)))

df.to_csv("Sportsbook.csv", index=False)


