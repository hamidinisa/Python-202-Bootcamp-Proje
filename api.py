from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from library import Library

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

library = Library("library.json")

class BookRequest(BaseModel):
    isbn: str

class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str
    cover_url: str

@app.get("/books", response_model=list[BookResponse])
def get_books():
    return library.list_books()

@app.post("/books", response_model=BookResponse)
def add_book(request: BookRequest):
    book = library.add_book(request.isbn)  # sadece ISBN gönderiyoruz
    if book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    return book

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    library.remove_book(isbn)
    return {"detail": "Kitap silindi."}
