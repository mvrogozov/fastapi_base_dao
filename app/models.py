from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    name: str = Field(unique=True, index=True)
    author_id: int | None = Field(
        foreign_key='person.id',
        primary_key=True
    )
    author: Optional['Person'] = Relationship(
        back_populates='author'
    )


class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(index=True)
    surname: str = Field(index=True)
    books: list['Book'] = Relationship(back_populates='books')
