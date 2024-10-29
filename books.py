from flask import jsonify
from typing import Optional, Any
from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from bson.objectid import ObjectId
import pymongo
import os

class Book(BaseModel):
    #book_id: ObjectId()
    author: Optional[str]
    title: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "author": "allan kanyenda",
                "title": "the running monk"
            }
        }

app = FastAPI()

@app.get("/status")
def checkStatus():
    return {"status": "up and running"}

def getDb():
    MONGODB_HOST = os.getenv('MONGODB_HOST')
    if MONGODB_HOST is None:
        MONGODB_HOST = 'localhost'
         
    client = pymongo.MongoClient(MONGODB_HOST,27017)
    db = client.BookDB
    print("Database created")
    print(f"{db.name}")
    # Add some data to database
    books_collection = db["books"]
    book = {"author": "alpucino", "title":"the devil wears platform shows"}
    books_collection.insert_one(book)
    return db

db = getDb()

@app.get("/")
def index():
    return "Welcome to the Books universium"

@app.get("/books")
def getBooks():
    books = []
    _books = db.books_collection.find()
    for book in _books:
        books.append({book["title"],book["author"]})
    return JSONResponse(jsonable_encoder(books))

@app.post("/books/{author}/{title}", status_code=status.HTTP_201_CREATED)
def createBook(author: str, title: str):
    book = Book()
    book.author = author
    book.title = title
    result = db.books_collection.insert_one(book.dict())
    if result.acknowledged:
        return {"Message": "Book added", "author": author}
    else:
        return {"Message": "Could not create book"}

@app.get("/books/{id}", status_code=status.HTTP_200_OK)
def getBook():
    book = db.books_collection.find_one({'id': id})
    return JSONResponse(jsonable_encoder(book))

@app.delete("/books/{id}")
def deleteBook():
    result = db.books_collection.delete_one({"id": id})
    if result.acknowledged:
        return {"Message": "Book deleted"}
    else:
        return {"Message": "Could not delete book"}
