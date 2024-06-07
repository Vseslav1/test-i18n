import os
from bs4 import BeautifulSoup


def find_tags(directory, metk, tags):
    """Функция ищет теги в .html файлах без определённой метки

    :параметр directory - директория для поиска HTML файлов.
    :параметр metk - название метки для поиска.
    :параметр tags - список тегов для поиска."""

    for root, dirs, files in os.walk(directory):
        """Ищем все .html файлы"""
        for file_name in files:
            if file_name.endswith(".html"):
                file_path = os.path.join(root, file_name)
                """открываем файлы в кодировке utf-8"""
                with open(file_path, 'r', encoding="utf-8") as file:
                    html = file.readlines()
                    """выводим строки с их номером"""
                    for number_of_line, html in enumerate(html, start=1):
                        for tag in tags:
                            if tag in html:
                                """передаём файлы .html в BeautifulSoup"""
                                soup = BeautifulSoup(html, "html.parser")
                                """проходимся по тегам"""
                                for elem in soup.find_all(tag):
                                    if not elem.has_attr(metk):
                                        print(f"тэг {tag} "
                                              f"не имеет метки - {metk},"
                                              f" в файле - {file_name},"
                                              f"в строке - {number_of_line},"
                                              f"строка - {elem}")


list_tg = ['p', 'h', 'h2', 'button']
find_tags("C:/Users/USER/PycharmProjects/test-i18n/app", 'i18n', list_tg)
