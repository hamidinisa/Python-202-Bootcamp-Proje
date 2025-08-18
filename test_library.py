
import os
import json
import pytest
from book import Book
from library import Library

TEST_FILE = "test_library.json"

@pytest.fixture
def library():
    # Her testten önce temiz bir test dosyası yarat
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    lib = Library(TEST_FILE)
    return lib

def test_add_book(library):
    book = Book("1984", "George Orwell", "12345")
    library.add_book(book)

    assert len(library.books) == 1
    assert library.books[0].title == "1984"

def test_remove_book(library):
    book = Book("1984", "George Orwell", "12345")
    library.add_book(book)

    library.remove_book("12345")
    assert len(library.books) == 0

def test_find_book(library):
    book = Book("1984", "George Orwell", "12345")
    library.add_book(book)

    found = library.find_book("12345")
    assert found is not None
    assert found.title == "1984"

def test_save_and_load_books(library):
    book1 = Book("1984", "George Orwell", "12345")
    book2 = Book("Animal Farm", "George Orwell", "67890")
    library.add_book(book1)
    library.add_book(book2)

    # Yeni bir kütüphane nesnesi açıp dosyadan yüklensin
    new_lib = Library(TEST_FILE)
    assert len(new_lib.books) == 2
    assert new_lib.find_book("12345").title == "1984"
    assert new_lib.find_book("67890").title == "Animal Farm"
