from fastapi import FastAPI, Query, Depends
import uvicorn
import requests
from typing import Optional
from datetime import date
from pydantic import BaseModel

app = FastAPI()

class HotelsSearchArgs:
    def __init__(
            self,
            hotel_id: int,
            date_from: date,
            date_to: date,
            location: str,
            has_spa: Optional[bool] = None,
            stars: Optional[int] = Query(None, ge=1, le=5),
    ):
        self.hotel_id = hotel_id
        self.date_from = date_from
        self.date_to = date_to
        self.location = location
        self.has_spa = has_spa
        self.stars = stars


@app.get('/')
async def root():
    return {'message': 'Hello, world!'}

class SHotel(BaseModel):
    address: str
    name: str
    stars: int

@app.get('/hotels/{hotel_id}', response_model=list[SHotel])
def get_hotels(
    search_args: HotelsSearchArgs = Depends()
): # or write here '-> list[SHotel]'
    hotels = [
        {
            'address': 'gagarina',
            'name': 'superhotel',
            'stars': 5
        }
    ]
    return search_args

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post('/booking')
def add_booking(booking: SBooking):
    pass

# r = requests.get(
#     'http://127.0.0.1:8000/hotels/123',
#     params = {'date_from': 'today', 'date_to': 'tomorrow'}
#     )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

# 1) git add 
# 2) git commit 
# 3) git remote 
# 4) git push