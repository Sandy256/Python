from time import sleep
import requests
from bs4 import  BeautifulSoup

url = 'https://telemetr.me/channels'

with requests.Session() as se:
    se.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en"
    }
    resp = se.get(url)

index = BeautifulSoup(resp.content, 'html.parser')

max_page = int(input('Ведите предпологаемое количество страниц: '))
pages = []
input_category = input('Введите категорию. (Учитывая регист как на сайте): ')

for x in range(1, max_page +1):
    sleep(3)
    sort = pages.append(se.get(f'http://telemetr.me/channels/cat/{input_category}/?page=' + str(x)))

for sort in pages:
    pars = BeautifulSoup(sort.content, 'html.parser')

    for el in pars.select('.wd-300'):
        link = el.find('a')
        try:
            print(link.get('href'))
            with open(f'{input_category}.txt', '+a') as file:
                file.write(f'{link.get("href")}\n')

        except AttributeError as error:
            print(f'Произошла ошибка{error}. Работа скрипта продолжаетсяю')
            continue



