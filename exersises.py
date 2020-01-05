"""
Цель: Создать программу поисковик Пользователь вводит тему, стартовую точку (google.com, yandex.ru, ...),
количество, рекурсивный поиск или нет
Программа находит в интернете начиная от стартовой точки все ссылки
на веб-странице и выводит в терминал
Реализовать программу в виде одной или нескольких функций
Собрать пакет для последующего использования
"""

import requests
from bs4 import BeautifulSoup

user_request = input("Какой у вас запрос?\n").replace(" ", "+")
url_search = f'https://google.com/search?q={user_request}'  # какой у запроса url


def main():
    request = requests.get(url_search)  # делаем запрос по этому url
    with open("index.html", "w", encoding="utf8") as f:
        f.write(request.text)
    with open("index.html", encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        all_a = soup.find_all("div", class_="ZINbbc xpd O9g5cc uUPGi")
        for elem in all_a:
            link_line = elem.find("div", class_="kCrYT")
            try:
                print(link_line.find('a').get('href')[7::].split('&')[0])
            except AttributeError:
                pass


main()


