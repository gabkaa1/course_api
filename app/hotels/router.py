

from fastapi import APIRouter


router = APIRouter(prefix='/hotels')

@router.get('')
def get_hotels():
    ...

@router.get('/hotels/id/{hotel_id}')
async def get_current_hotel():
    ...