from app.database import Base
from sqlalchemy import JSON, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Hotels(Base):
    __tablename__ = 'hotels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str]
    services = Column(JSON)
    room_quantity: Mapped[int]
    image_id: Mapped[int]


