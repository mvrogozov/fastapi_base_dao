from app.repositories.book_repo import BookRepository
from app.schemes import BookCreateScheme, BookFilterScheme


class BookService:

    def __init__(self):
        self.book_repository = BookRepository()

    async def create_book(self, book: BookCreateScheme):
        return await self.book_repository.add(book)

    async def get_books(self, filters: BookFilterScheme):
        return await self.book_repository.find_all(filters)

    async def get_book_by_id(self, book_id: int):
        return await self.book_repository.find_one_or_none_by_id(book_id)
