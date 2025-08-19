from app.repositories.person_repo import PersonRepository
from app.schemas import PersonCreate


class PersonService:

    def __init__(self):
        self.repository = PersonRepository()

    async def person_create(self, person: PersonCreate):
        return await self.repository.add(person)
