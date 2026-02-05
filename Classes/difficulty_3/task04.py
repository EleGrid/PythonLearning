import unittest
from zlib import DEF_BUF_SIZE

"""
Задача: Книжная полка (List filtering)

Создайте класс `Bookshelf`.
У него есть список книг `books`. Каждая книга - это словарь `{"title": "...", "genre": "..."}`.
Добавьте метод `add_book(title, genre)` для добавления книги.
Добавьте метод `get_books_by_genre(genre)`, который возвращает список названий (title) книг определенного жанра.

Пример:
    >>> shelf = Bookshelf()
    >>> shelf.add_book("Harry Potter", "Fantasy")
    >>> shelf.add_book("Hobbit", "Fantasy")
    >>> shelf.add_book("Python Guide", "Education")
    >>> shelf.get_books_by_genre("Fantasy")
    ['Harry Potter', 'Hobbit']
"""

class Bookshelf:
    def __init__(self):
        self.books =[]

    def add_book(self, title, genre):
        book = {}
        book["title"] = title
        book["genre"] = genre
        self.books.append(book)

    def get_books_by_genre(self, genre):
        new_list = []
        for book_2 in self.books:
            if book_2["genre"] == genre:
                new_list.append(book_2["title"])
        return new_list


class TestBookshelf(unittest.TestCase):
    def test_search_genre(self):
        b = Bookshelf()
        b.add_book("A", "Sci-Fi")
        b.add_book("B", "Sci-Fi")
        b.add_book("C", "Drama")
        found = b.get_books_by_genre("Sci-Fi")
        self.assertEqual(found, ["A", "B"])

    def test_not_found(self):
        b = Bookshelf()
        b.add_book("A", "Sci-Fi")
        found = b.get_books_by_genre("Comedy")
        self.assertEqual(found, [])

    def test_empty(self):
        b = Bookshelf()
        self.assertEqual(b.get_books_by_genre("Any"), [])

if __name__ == "__main__":
    unittest.main()
