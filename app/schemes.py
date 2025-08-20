from pydantic import BaseModel, Field
from sqlmodel import SQLModel

from app.models import Book


class BookCreateScheme(BaseModel):
    name: str
    author_id: int | None


class PersonCreateScheme(BaseModel):
    name: str
    surname: str


class PersonFilterScheme(BaseModel):
    name: str | None = None
    surname: str | None = None

    # class Config:
    #     extra = 'allow'


class PersonWithBooksScheme(BaseModel):
    name: str
    surname: str
    books: list[Book]


class BookFilterScheme(BaseModel):
    name: str | None = None
    author_id: int | None = None
