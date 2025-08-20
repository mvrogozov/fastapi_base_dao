from pydantic import BaseModel

from app.repositories.person_repo import PersonRepository
from app.schemes import PersonCreateScheme


class PersonService:

    def __init__(self):
        self.repository = PersonRepository()

    async def person_create(self, person: PersonCreateScheme):
        return await self.repository.add(person)

    async def get_persons(self, filters: BaseModel | None):
        return await self.repository.find_all(filters)

    async def get_person_by_id(self, person_id: int):
        return await self.repository.find_one_or_none_by_id(person_id)

    async def get_person_with_books_by_id(self, person_id: int):
        return await self.repository.find_person_with_books_by_id(person_id)
