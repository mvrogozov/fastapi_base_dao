from app.repositories.book_repo import BookRepository
from app.schemas import BookCreate


class BookService:

    def __init__(self):
        self.book_repository = BookRepository()

    async def create_book(self, book: BookCreate):
        return await self.book_repository.add(book)
