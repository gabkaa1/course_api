from fastapi import APIRouter, Request, Depends
from sqlalchemy import select


from app.database import async_session_maker
from app.bookings.models import Bookings
from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix='/bookings',
    tags=['Бронирования'],
)


@router.get('')
async def get_bookings(user: Users = Depends(get_current_user)):
    # print(request.cookies)
    # return dir(request) 
    # print(user, type(user), user.email)
    # return user
    return await BookingDAO.find_all(user_id=user.id)
    # return await BookingDAO.find_all()
    # async with async_session_maker() as session:
    #     query = select(Bookings)
    #     result = await session.execute(query)
    #     return result.mappings().all()

