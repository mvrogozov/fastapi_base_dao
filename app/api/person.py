from typing import Annotated

from fastapi import APIRouter, Depends

from app.models import Person
from app.schemas import PersonCreate
from app.services.person_service import PersonService


router = APIRouter(
    prefix='/persons',
    tags=['persons']
)


@router.post(
    '/',
    response_model=Person,
    summary='create book'
)
async def create_book(
    person: PersonCreate,
    person_service: Annotated[PersonService, Depends()]
):
    return await person_service.person_create(person)
