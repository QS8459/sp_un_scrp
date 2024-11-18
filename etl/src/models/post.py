from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey;
from sqlalchemy import String, BigInteger;
from datetime import datetime;
from .base import BaseModel;
from pydantic.types import UUID;

class Posts(BaseModel):
    __tablename__ = 'posts'
    __table_arg__ = {"schema": "public"}

    post_id: Mapped[int] = mapped_column(nullable=True, unique = True)
    title: Mapped[String] = mapped_column(String(250), nullable=True, default=None)
    image_url: Mapped[String] = mapped_column(String(300),nullable=True)
    link: Mapped[String] = mapped_column(String(200), nullable= True, default = None)
    description: Mapped[String] = mapped_column(String(550), nullable=True, default=None)
    source: Mapped[UUID] = mapped_column(ForeignKey('source.id'))
    category: Mapped[UUID] = mapped_column(ForeignKey('category.id'))
    posted_on: Mapped[datetime] = mapped_column(nullable=True)


__all__ = "Posts"
