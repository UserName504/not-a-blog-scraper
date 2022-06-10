import json
import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
from random import randrange
import os

today = dt.today()
currentYear = today.year
years = range(2005, currentYear+1)
year = randrange(2005, currentYear+1)
months = range(1,13)
month = randrange(1, 13)
todaysDate = today.strftime("%B %d, %Y")

def printYears():
    for year in years:
        return year

def getMonths():
    for month in months:
        return month

def extract():
    url = f'https://georgerrmartin.com/notablog/{year}/{month}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def notABlog(soup):
    divs = soup.find_all('div', class_ = 'post-main')
    try:
        for item in divs:
            title = item.find('a').text
            date = item.find('div', class_ = 'thedate').text
            print(f'{title}, {date}')
    except:
        print(f'There were no blogs in {month} of {year}.')
    if len(divs) > 1:
        print(f'\nThere were {len(divs)} blogs in {month}, {year}.')
    elif len(divs) < 2:
        print(f'\nThere was {len(divs)} blog in {month}, {year}.')

content = extract()
print(notABlog(content))
