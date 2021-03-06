import os
import csv
import json
import sqlite3
import requests
from random import randrange
from bs4 import BeautifulSoup
from datetime import datetime as dt

today = dt.today()
current_year = today.year
years = range(2005, current_year+1)
year = randrange(2005, current_year+1)
months = range(1,13)
month = randrange(1, 13)
todays_date = today.strftime("%B %d, %Y")

def get_years():
    for year in years:
        return year

def get_months():
    for month in months:
        return month

def extract():
    url = f'https://georgerrmartin.com/notablog/{year}/{month}/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def not_a_blog(soup):
    divs = soup.find_all('div', class_ = 'post-main')
    try:
        for item in divs:
            title = item.find('a').text
            date = item.find('div', class_ = 'thedate').text
            #
            date_length = len(date)
            #
            print(f'{title}, {date}')

    except:
        return f'There were no blogs in {month} of {year}.'
    if len(divs) > 1:
        return f'\nThere were {len(divs)} blogs in {month}, {year}.'
    #elif len(divs) < 2:
    elif len(divs) == 1:
        return f'\nThere was {len(divs)} blog in {month}, {year}.'

content = extract()
print(not_a_blog(content))
#not_a_blog(content)
"""
def not_a_blog(soup):
    divs = soup.find_all('div', class_ = 'post-main')
    try:
        for item in divs:
            title = item.find('a').text
            date = item.find('div', class_ = 'thedate').text
            #print(f'{title}, {date}')
            with open('not_a_blog_scraper.csv', 'w') as csvfile:
                fieldnames = ['Title', 'Date']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Title': {title}, 'Date': {date}})
    except:
        print(f'There were no blogs in {month} of {year}.')
    if len(divs) > 1:
        return f'\nThere were {len(divs)} blogs in {month}, {year}.'
    elif len(divs) < 2:
        return f'\nThere was {len(divs)} blog in {month}, {year}.'

content = extract()
print(not_a_blog(content))
"""
