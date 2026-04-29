from fastapi import Body,FastAPI
from typing import Optional,List 
from pydantic import BaseModel, Field

app=FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating

class BookRequest(BaseModel):
    id:int
    title:str=Field(min_length=1)
    author:str=Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=-1,lt=6)

BOOKS = [
    Book(1, "Atomic Habits", "James Clear", "Build good habits and break bad ones", 5),
    Book(2, "Deep Work", "Cal Newport", "Focus deeply in a distracted world", 5),
    Book(3, "Clean Code", "Robert C. Martin", "Guide to writing clean and maintainable code", 5),
    Book(4, "The Alchemist", "Paulo Coelho", "A journey of self-discovery", 4),
    Book(5, "Think and Grow Rich", "Napoleon Hill", "Principles for personal success", 4)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

#post request before data validation
@app.post("/create_book")
async def create_book(book_request=Body()):
    BOOKS.extend([book_request])
    return book_request

#post request after data validation
@app.post("/create_book_with_validation")
async def create_book_with_validation(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.extend([new_book])
    return book_request