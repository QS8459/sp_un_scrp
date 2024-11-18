from sqlalchemy import create_engine, MetaData;
from sqlalchemy.orm import sessionmaker;
from contextlib import contextmanager;
from src.configs import settings;
from sqlalchemy.exc import SQLAlchemyError
from typing import ContextManager;

engine = create_engine(str(settings.pg_uri));
Session = sessionmaker(bind = engine);
metadate = MetaData();

@contextmanager
def session() -> ContextManager[Session]:
    session = Session();
    try:
        yield session;
        # session.commit();
    except SQLAlchemyError as e:
        session.rollback();
        raise e;
    finally:
        session.close();
