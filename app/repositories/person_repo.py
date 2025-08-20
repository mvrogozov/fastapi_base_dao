from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import selectinload

from app.base import BaseDAO
from app.models import Person
from app.database import get_session


class PersonRepository(BaseDAO):
    model = Person

    async def find_person_with_books_by_id(self, data_id: int):
        try:
            async with get_session() as session:
                query = select(self.model).filter_by(id=data_id).options(
                    selectinload(self.model.books)
                )
                result = await session.exec(query)
                return result.scalar_one_or_none()
        except SQLAlchemyError:
            raise
    # async def get_person_books(self, person_id: int):
    #     async with get_session() as session:
    #         query = select(self.model).filter_by('')
