user_request = input("Какой у вас запрос?\n").replace(" ", "+")
links_number = int(input("Сколько ссылок показать?\n")) + 1
url_search = f'https://google.com/search?q={user_request}'
