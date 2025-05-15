from app.utils.db import Base
from sqlalchemy import Integer, Text, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.users.models.orm.user import UserDBModel
from app.core.listings.models.orm.category import CategoryDBModel
from datetime import datetime
from sqlalchemy.sql import func
from decimal import Decimal


class ListingDBModel(Base):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False
    )
    image_urls: Mapped[list[str]] = mapped_column(Text, nullable=False)

    # Relationships
    user_id: Mapped["UserDBModel"] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["UserDBModel"] = relationship(back_populates="listings")

    category_id: Mapped["CategoryDBModel"] = mapped_column(
        Integer, ForeignKey("categories.id"), nullable=False
    )
