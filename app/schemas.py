from pydantic import BaseModel, Field
from sqlmodel import SQLModel


class BookCreate(BaseModel):
    name: str
    author_id: int | None


class PersonCreate(BaseModel):
    name: str
    surname: str
