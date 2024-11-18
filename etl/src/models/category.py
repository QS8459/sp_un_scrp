from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column;
from enum import Enum;
from src.models.base import BaseModel;

class CategoryEnum(Enum):
    BUSINESS:str ='BUSINESS';
    FINANCE:str = 'FINANCE';
    ECONOMY:str = "ECONOMY";
    PRIVATE_BUSINESS:str = "PRIVATE_BUSINESS";
    STARTUP:str = "STARTUP";
    TECH:str = "TECH";
    ENERGY:str = "ENERGY"
    BLOCKCHAIN_CRYPTO:str = "BLOCKCHAIN_CRYPTO";
    GOVERNMENT:str = "GOVERNMENT";
    SOCIAL:str = "SOCIAL";
    EDUCATION:str = "EDUCATION";
    TRANSPORT:str = "TRANSPORT";
    ENTREPRENEUR:str = "ENTREPRENEUR";
    PERSON:str = "PERSON";
    INTERVIEW:str = "INTERVIEW";
    MARKETING:str = "MARKETING";
    POLITICS:str = "POLITICS";
    SPORT:str = "SPORT"
    CRIME:str = "CRIME";
    OTHER:str = "OTHER";

class Category(BaseModel):
    __tablename__ = "category";
    __table_argS__ = {"schema":"public"}

    label:Mapped[String] = mapped_column(String(20), default = CategoryEnum.OTHER)

__all__ = ("Category", "CategoryEnum")


