from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query

from app.models import Person
from app.schemes import (
    PersonCreateScheme, PersonFilterScheme, PersonWithBooksScheme
)
from app.services.person_service import PersonService


router = APIRouter(
    prefix='/persons',
    tags=['persons']
)


@router.post(
    '/',
    response_model=Person,
    summary='create person'
)
async def create_book(
    person: PersonCreateScheme,
    person_service: Annotated[PersonService, Depends()]
):
    return await person_service.person_create(person)


@router.get(
    '/',
    response_model=list[Person],
    summary='get all persons'
)
async def get_persons(
    person_service: Annotated[PersonService, Depends()],
    filters: Annotated[PersonFilterScheme, Depends()]
):
    return await person_service.get_persons(filters)


@router.get(
    '/{person_id}',
    response_model=Person | None,
    summary='get person by id'
)
async def get_person(
    person_service: Annotated[PersonService, Depends()],
    person_id: int = Path(
        ..., gt=0, description='person ID'
    )
):
    return await person_service.get_person_by_id(person_id)


@router.get(
    '/{person_id}/with-books',
    response_model=PersonWithBooksScheme | None,
    summary='get person with books by id'
)
async def get_person_with_books(
    person_service: Annotated[PersonService, Depends()],
    person_id: int = Path(
        ..., gt=0, description='person ID'
    )
):
    return await person_service.get_person_with_books_by_id(person_id)
