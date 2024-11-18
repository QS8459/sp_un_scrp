from sqlalchemy import select, between;
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.crud.base import BaseService;
from src.models.post import Posts
from src.db.engine import session;

class PostsService(BaseService):
    def __init__(self, session):
        super().__init__(session, Posts);

    def get_in_date_range(self, **kwargs):
        try:
            with self.session as s:
                query = select(self.model).where(self.model.posted_on.between(kwargs.get('start_date'),kwargs.get('end_date')));
                res = s.execute(query);
                return res.scalars().all()
        except SQLAlchemyError as e:
            raise e;

def post_service():
    service = PostsService(session())
    return service;
    # a.add(**kwargs);
