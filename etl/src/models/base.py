from sqlalchemy import String, func, DateTime;
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase;
from pydantic.types import UUID4
from uuid import uuid4
from datetime import datetime;
class BaseModel(DeclarativeBase):

    id:Mapped[UUID4] = mapped_column(primary_key=True, default=uuid4);
    created_at:Mapped[DateTime] = mapped_column(DateTime(timezone=True), default = datetime.utcnow());

    # def __repr__(self):
    #     return f'<{self.__class__.__name__}(id={self.uuid})>'
    #
    # def __str__(self):
    #     return f'<{self.__class__.__name__}(id={self.uuid})>'





