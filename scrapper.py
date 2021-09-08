from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import csv

find_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
driver = webdriver.Edge("./edgedriver/msedgedriver.exe")
webpage = requests.get(find_url)
time.sleep(20)

soup = BeautifulSoup(webpage.text,'html.parser')

Star_name = []
Distance =[]
Mass = []
Radius =[]

temp_list= []

def scrape():
    table_tag = soup.find_all('table')
    
    tr_tags = table_tag[4].find_all('tr')
    for tr_tag in tr_tags:
        td_tags = tr_tag.find_all('td')
        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)

    for i in range(0, 200):
        Star_name.append(temp_list[i][0])
        Distance.append(temp_list[i][5])
        Mass.append(temp_list[i][8])
        Radius.append(temp_list[i][9])

    data = pd.DataFrame(list(Star_name, Distance, Mass, Radius), columns = ['Star_name', 'Distance', 'Mass', 'Radius'])
    print(data)

    data.to_csv('list_of_stars.csv')

scrape()