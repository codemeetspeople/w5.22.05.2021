import json
import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
BOOKS_PATH = os.path.join(PROJECT_ROOT, 'books')


class Book:
    def __init__(self, title=None):
        self._author = None
        self._title = None
        self._changed = False

        if title:
            self.load(title)

    @property
    def author(self):
        return self._author

    @property
    def title(self):
        return self._title

    @author.setter
    def author(self, value):
        self._author = value
        self._changed = True

    @title.setter
    def title(self, value):
        self._title = value
        self._changed = True

    def save(self):
        if self._changed:
            book_info = {'author': self.author, 'title': self.title}
            with open(os.path.join(BOOKS_PATH, f'{self.title}.txt'), 'w') as f:
                f.write(json.dumps(book_info))
        self._changed = False

    def load(self, title):
        try:
            book_title = f'{title}.txt'
            with open(os.path.join(BOOKS_PATH, book_title), 'r') as f:
                book_info = json.loads(f.read())
            self._title = book_info['title']
            self._author = book_info['author']
        except FileNotFoundError:
            print(f'{title} not found. Empty {self.__class__.__name__} object was created.')


if __name__ == '__main__':
    book = Book('Java from HELL!')
