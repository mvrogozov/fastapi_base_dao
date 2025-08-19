from app.base import BaseDAO
from app.models import Book


class BookRepository(BaseDAO):
    model = Book
