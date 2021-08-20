from bs4 import BeautifulSoup as BS
from re import compile
from time import sleep
from random import uniform
from utils import url_open

SNILS = '<SNILS>'

URL = 'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/'

def get_urls(url):
    bs = BS(url_open(url))
    for a in bs.find_all('a', href=compile('ru\/abiturientam\/priyom-na-1-y-kurs\/podavshie-zayavlenie\/ochnaya\/byudzhet\/.+')):
        yield 'https://etu.ru/' + a.attrs['href']

def get_positions(urls):
    positions = {}
    for url in urls:
        bs = BS(url_open(url))
        tables = [[int(td.text) if td.text.isdigit() else td.text for td in tr.find_all('td')] for tr in bs.find_all('tr', class_='')]
        for table in tables:
            if SNILS in table:
                edu_name = bs.find('h1', class_='page-header').text
                positions[edu_name] = table[0]
        sleep(uniform(10.0, 20.0))
    return positions

with open('spbgetu.txt', 'w') as file:
    file.write('SNILS: {}\n'.format(SNILS))
    for edu_name, position in get_positions(get_urls(URL)).items():
        file.write('{}: {}\n'.format(edu_name, position))
