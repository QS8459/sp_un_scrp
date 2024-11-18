from src.crud.base import BaseService;
from src.models.source import Source
from src.db.engine import session;


class SourceService(BaseService):
    def __init__(self, session):
        super().__init__(session, Source);

def source_service():
    service = SourceService(session())
    return service