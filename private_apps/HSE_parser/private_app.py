import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/78.0.3904.97 Safari/537.36'}

base_url = 'https://social.hse.ru/persons'


def hse_parse(base_url, headers):
    session = requests.session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        links = soup.find_all('div', attrs={'class': 'fa-person__item'})
        links_arr = []

        for link in links:
            result = link.find('a', attrs={'class': 'fa-person__name'})['href']
            links_arr.append(result)

        print(links_arr)

    else:
        print('ERROR')


hse_parse(base_url, headers)
