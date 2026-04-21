from app.database import Base
from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Computed
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date

class Bookings(Base):
    __tablename__ = 'bookings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey('rooms.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    date_from: Mapped[date] = mapped_column(nullable=False)
    date_to: Mapped[date] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    total_cost: Mapped[int] = mapped_column(Computed('(date_to-date_from)*price'))
    total_days: Mapped[int] = mapped_column(Computed('date_to-date_from'))