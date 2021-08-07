from requests import get
from bs4 import BeautifulSoup
from random import uniform
from time import sleep
ID = '{ID}'
HEADERS = {
    'user-agent': '{USER-AGENT}'
}
EDUCATION_PROGRAMS = {
    'Программная инженерия': 'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/ochnaya/byudzhet/programmnaya-inzheneriya',
    'Прикладная математика и информатика': 'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/ochnaya/byudzhet/prikladnaya-matematika-i-informatika',
    'Информатика и вычислительная техника (Искусственный интеллект)': 'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/ochnaya/byudzhet/informatika-i-vychislitelnaya-tehnika-ii',
    'Информационные системы и технологии': 'https://etu.ru/ru/abiturientam/priyom-na-1-y-kurs/podavshie-zayavlenie/ochnaya/byudzhet/informacionnye-sistemy-i-tehnologii'
}
f = open('spbgetu.txt', 'w')
f.write('СНИЛС: {}\n'.format(ID))
for name, link in EDUCATION_PROGRAMS.items():
    response = get(link, headers=HEADERS)
    bs = BeautifulSoup(response.text)
    persons = [[td.text for td in tr.findAll('td')] for tr in bs.findAll('tr', {'class': ''})]
    for person in persons:
        if ID in person:
            f.write(
                '{}: {}\n'.format(
                    name,
                    person[0]
                )
            )
    sleep(uniform(25.0, 50.0))
f.close()
