from typing import Generic, TypeVar, Type;
from src.db.engine import sessionmaker;
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import select, and_;
from abc import ABC
T = TypeVar("T");

class BaseService(ABC, Generic[T]):
    def __init__(self,session, model:Type[T]):
        self.session = session;
        self.model = model;

    def add(self, **kwargs):
        try:
            with self.session as s:
                instance = self.model(**kwargs);
                s.add(instance);
                s.commit();
        except IntegrityError:
            print("IntegrityError")
            s.rollback()
        except SQLAlchemyError as e:
            s.rollback()

    def get(self, **kwargs):
        try:
            with self.session as s:
                query = select(self.model)
                if kwargs:
                    conditions = [getattr(self.model, key) == value for key,value in kwargs.items()]
                    query = query.where(and_(*conditions))
                res = s.execute(query);
                return res.scalars().first()
        except SQLAlchemyError as e:
            raise e

    def get_all(self):
        try:
            with self.session as s:
                query = select(self.model);
                res = s.execute(query)
                return res.scalars().all();
        except SQLAlchemyError as e:
             raise e;

