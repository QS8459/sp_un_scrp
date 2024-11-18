from src.crud.base import BaseService;
from src.models.category import Category;
from src.db.engine import session;

class CategoryService(BaseService):
    def __init__(self,session):
        super().__init__(session, Category);


def category_service():
    service = CategoryService(session());
    return service;