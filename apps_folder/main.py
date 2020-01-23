import logging
import requests
from bs4 import BeautifulSoup
from search_package.users_data import url_search, links_number


def main():
    """
    Функция ищет ссылки на странице с запросом и выводит в терминал
    url_search - адрес запроса
    links_number - количество ссылок
    """

    logging.basicConfig(filename="sample.log",
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO)
    try:
        request = requests.get(url_search)
        request.raise_for_status()
        with open("index.html", "w", encoding="utf8") as f:
            f.write(request.text)

    except requests.RequestException:
        logging.info("Ошибка в запросе")

    with open("index.html", encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        all_a = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")

    s = 1
    for elem in all_a:
        link_line = elem.find("div", class_="kCrYT")
        try:
            if s == links_number:
                break
            print(link_line.find('a').get('href')[7::].split('&')[0])
            s += 1
        except (AttributeError):
            logging.info("Пропуск неподходящей ссылки")