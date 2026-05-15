from fastapi import HTTPException, status

class BookingException(HTTPException):
    status_code=500
    detail=''

    def __init__(self, status_code: int = 500, detail: str = ''):
        super().__init__(status_code=status_code, detail=detail)
    # def __init__(self):
    #     super().__init__(status_code=self.status_code, detail=self.detail)



class UserAlreadyExistsExeption(BookingException):
  def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
              detail='Пользователь уже существует'
              )
        
  


class IncorrectEmailOrPasswordException(BookingException):
  def __init__(self):
        super().__init__(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail = 'Неверная почта или пароль'
        )
  
 

class TokenExpireException(BookingException):
  def __init__(self):
        super().__init__(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail = 'Токен истек'
        )
  

class TokenAbsentException(BookingException):
  def __init__(self):
        super().__init__(
           status_code=status.HTTP_401_UNAUTHORIZED,
  detail = 'Токен отсутствует'
        )
  
 

class IncorrectTokenFormatException(BookingException):
  def __init__(self):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
            detail = 'Неверный формат токена'
            
        )
  
 

class UserIsNotPresentException(BookingException):
  def __init__(self):
        super().__init__(
           status_code=status.HTTP_401_UNAUTHORIZED,
        )
  

class RoomCannotBeBooked(BookingException):
  def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail='Не осталось свободных номеров'
        )
