from fastapi import APIRouter
from sqlalchemy import select


from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('', response_model=list[SBooking])
async def get_bookings():
    return await BookingDAO.find_all()
    # async with async_session_maker() as session:
    #     query = select(Bookings)
    #     result = await session.execute(query)
    #     return result.mappings().all()

