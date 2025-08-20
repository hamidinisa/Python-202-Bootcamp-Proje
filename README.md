Global AI Hub Python 202 Bootcamp Proje
Library Project

Library Project, ISBN kullanarak kitap ekleme, listeleme ve silme işlemleri yapabilen bir FastAPI uygulamasıdır. Kitap bilgileri Open Library API üzerinden otomatik çekilir.

 Özellikler

Kitap ekleme sadece ISBN ile yapılır.

Open Library API kullanılarak title, author ve kapak görseli otomatik alınır.

Eklenen kitaplar JSON dosyasında saklanır (library.json).

Kitapları listeleme ve silme işlemleri mevcut.

Swagger UI ile kolay test ve dokümantasyon.

 Gereksinimler

Python 3.10+

Virtualenv (opsiyonel ama tavsiye edilir)

Kütüphaneler: fastapi, uvicorn, requests, pydantic

Kurulum için:

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install fastapi uvicorn requests

 Çalıştırma

Projenin bulunduğu dizinde:

uvicorn api:app --reload


Sunucu varsayılan olarak: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

API Endpoints
1. GET /books

Tüm kitapları listeler.

Response Örneği:

[
  {
    "title": "Matilda",
    "author": "Roald Dahl",
    "isbn": "9780140328721",
    "cover_url": "https://covers.openlibrary.org/b/id/8156191-M.jpg"
  }
]

2. POST /books

Sadece ISBN ile kitap ekler. Open Library API’den diğer bilgiler otomatik alınır.

Request Body:

{
  "isbn": "9780140328721"
}


Response Örneği:

{
  "title": "Matilda",
  "author": "Roald Dahl",
  "isbn": "9780140328721",
  "cover_url": "https://covers.openlibrary.org/b/id/8156191-M.jpg"
}


ISBN geçerli değilse:

{
  "detail": "Kitap bulunamadı."
}

3. DELETE /books/{isbn}

ISBN’e göre kitap siler.

Response Örneği:

{
  "detail": "Kitap silindi."
}


Silinmek istenen kitap bulunamazsa:

{
  "detail": "Kitap bulunamadı."
}



Eğer dosya yoksa veya boşsa, otomatik olarak oluşturulur.

Örnek boş içerik:

[]
