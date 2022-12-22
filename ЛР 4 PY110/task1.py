import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"(?:#+ *(?P<position>\d+)\. *\[(?P<book>.+)\] *\((?P<book_url>http[s]?:\/\/\S+)\)" \
             r" *by *(?P<author>\b.+\b) *\((?P<recommended>\d+\.\d+%) recommended\)" \
             r" *\n+!\[\]\((?P<cover_url>http[s]?:\/\/www\S+)\) *\n+\"(?P<description>(?:.|\n)+?)\")"  # записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX)  # не использовал флаг re.DOTALL

    with open(BOOKS_FILE, encoding='utf-8') as f:  # добавил кодировку utf-8
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
