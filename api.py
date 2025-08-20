from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
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
    isbn: Optional[str] = None
    title: Optional[str] = None
    author: Optional[str] = None

class BookResponse(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    cover_url: Optional[str] = None

@app.get("/books", response_model=list[BookResponse])
def get_books():
    return library.list_books()

@app.post("/books", response_model=BookResponse)
def add_book(request: BookRequest):
    if not request.isbn and not request.title and not request.author:
        raise HTTPException(status_code=400, detail="En az bir alan (isbn, title veya author) girilmelidir.")
    book = library.add_book(isbn=request.isbn, title=request.title, author=request.author)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    return book

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    library.remove_book(isbn)
    return {"detail": "Kitap silindi."}
