# test_api.py
import pytest
from library import Library

def test_add_book_success(monkeypatch):
    """Başarılı API çağrısı testi"""

    class DummyResponse:
        status_code = 200
        def json(self):
            return {
                "title": "Test Kitabı",
                "authors": [{"key": "/authors/OL12345A"}]
            }

    class DummyAuthorResponse:
        status_code = 200
        def json(self):
            return {"name": "Test Yazar"}

    def fake_get(url, timeout=10):
        if "authors" in url:
            return DummyAuthorResponse()
        return DummyResponse()

    monkeypatch.setattr("httpx.get", fake_get)

    lib = Library("test.json")
    book = lib.add_book("1234567890")

    assert book is not None
    assert book.title == "Test Kitabı"
    assert book.author == "Test Yazar"
