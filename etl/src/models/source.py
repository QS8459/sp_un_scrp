from sqlalchemy import String;
from sqlalchemy.orm import Mapped, mapped_column;
from src.models.base import BaseModel;

class Source(BaseModel):
    __tablename__ = 'source';
    __table_arg__ = {'schema':'public'};

    name:Mapped[String] = mapped_column(String(20), nullable=False);

__all__ = 'Source';
