import json
import requests

class Library:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "r", encoding="utf-8") as f:
                content = f.read().strip()
                self.books = json.loads(content) if content else []
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        for book in self.books:
            if book["isbn"] == isbn:
                return book
        return None

    # sadece ISBN ile kitap ekle
    def add_book(self, isbn):
        # Open Library API çağrısı
        url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        response = requests.get(url)
        data = response.json()
        key = f"ISBN:{isbn}"
        if key not in data:
            return None

        book_data = data[key]
        title = book_data.get("title", "Bilinmiyor")
        authors = [a["name"] for a in book_data.get("authors", [])] or ["Bilinmiyor"]

        book = {
            "title": title,
            "author": ", ".join(authors),
            "isbn": isbn,
            "cover_url": book_data.get("cover", {}).get("medium", "")
        }

        self.books.append(book)
        self.save_books()
        return book

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b["isbn"] != isbn]
        self.save_books()

