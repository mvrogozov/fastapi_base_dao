from app.base import BaseDAO
from app.models import Person


class PersonRepository(BaseDAO):
    model = Person
