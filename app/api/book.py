from typing import Annotated

from fastapi import APIRouter, Depends

from app.services.book_service import BookService
from app.schemes import BookCreateScheme, BookFilterScheme
from app.models import Book


router = APIRouter(
    prefix='/books',
    tags=['books']
)


@router.post(
    '/',
    response_model=Book,
    summary='create book'
)
async def create_book(
    book: BookCreateScheme,
    book_service: Annotated[BookService, Depends()]
):
    return await book_service.create_book(book)


@router.get(
    '/',
    response_model=list[Book],
    summary='get all books'
)
async def get_books(
    book_service: Annotated[BookService, Depends()],
    filters: Annotated[BookFilterScheme, Depends()]
):
    return await book_service.get_books(filters)


@router.get(
    '/{book_id}',
    response_model=Book | None,
    summary='get book by ID'
)
async def get_book(
    book_service: Annotated[BookService, Depends()],
    book_id: int
):
    return await book_service.get_book_by_id(book_id)
