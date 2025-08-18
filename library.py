
import json
import os
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book: Book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn: str):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def list_books(self):
        if not self.books:
            print("Kütüphane boş!")
        for book in self.books:
            print(book)

    def find_book(self, isbn: str):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([vars(b) for b in self.books], f, ensure_ascii=False, indent=4)
