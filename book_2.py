from fastapi import Body,FastAPI
from typing import Optional,List 

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



BOOKS = [
    Book(1, "Atomic Habits", "James Clear", "Build good habits and break bad ones", 5),
    Book(2, "Deep Work", "Cal Newport", "Focus deeply in a distracted world", 5),
    Book(3, "Clean Code", "Robert C. Martin", "Guide to writing clean and maintainable code", 5),
    Book(4, "The Alchemist", "Paulo Coelho", "A journey of self-discovery", 4),
    Book(5, "Think and Grow Rich", "Napoleon Hill", "Principles for personal success", 4)
]

@app.get("/books")

def read_all_books():
    return BOOKS