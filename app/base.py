from typing import Generic, TypeVar

from sqlalchemy import exists
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlmodel import SQLModel
from pydantic import BaseModel

from app.database import get_session

T = TypeVar('T', bound=SQLModel)


class BaseDAO(Generic[T]):
    model: type[T] = None

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int):
        try:
            async with get_session() as session:
                query = select(cls.model).filter_by(id=data_id)
                result = await session.exec(query)
                return result.scalar_one_or_none()
        except SQLAlchemyError:
            raise

    @classmethod
    async def find_one_or_none(cls, filters: BaseModel | None):
        if filters:
            filter_dict = filters.model_dump(exclude_unset=True)
        else:
            filter_dict = []
        try:
            async with get_session() as session:
                query = select(cls.model).filter_by(**filter_dict)
                result = await session.exec(query)
                return result.scalar_one_or_none()
        except SQLAlchemyError:
            raise

    @classmethod
    async def find_all(cls, filters: BaseModel | None):
        if filters:
            filter_dict = filters.model_dump(
                exclude_unset=True,
                exclude_none=True
            )
        else:
            filter_dict = {}
        try:
            async with get_session() as session:
                query = select(cls.model).filter_by(**filter_dict)
                result = await session.exec(query)
                return result.scalars().all()
        except SQLAlchemyError:
            raise

    @classmethod
    async def add(cls, values: BaseModel):
        try:
            values_dict = values.model_dump(exclude_unset=True)
            async with get_session() as session:
                new_instance = cls.model(**values_dict)
                session.add(new_instance)
                await session.commit()
                await session.refresh(new_instance)
                return new_instance
        except SQLAlchemyError:
            raise

    @classmethod
    async def add_many(cls, instances: list[BaseModel]):
        values_list = [
            item.model_dump(exlude_unset=True) for item in instances
        ]
        new_instances = [cls.mode(**values) for values in values_list]
        try:
            async with get_session() as session:
                session.add_all(new_instances)
        except SQLAlchemyError:
            raise
