from sqlalchemy import Integer, Text, DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.utils.db import Base
from app.core.listings.models.orm.listing import ListingDBModel


class UserDBModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    listings: Mapped[list["ListingDBModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan", lazy="selectin"
    )
