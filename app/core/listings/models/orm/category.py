from app.utils.db import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.listings.models.orm.listing import ListingDBModel


class CategoryDBModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)

    # Relationships
    listings: Mapped[list["ListingDBModel"]] = mapped_column(
        back_populates="category", lazy="selectin"
    )
