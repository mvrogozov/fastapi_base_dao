from typing import Annotated

from fastapi import APIRouter, Depends

from app.services.book_service import BookService
from app.schemas import BookCreate
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
    book: BookCreate,
    book_service: Annotated[BookService, Depends()]
):
    return await book_service.create_book(book)
