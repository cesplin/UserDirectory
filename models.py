from pydantic import BaseModel, constr
from uuid import UUID, uuid4

class UserBase(BaseModel):
    display_name: str
class Phone(BaseModel):
    number: constr(pattern=r'^\+\d{1,3}\s\d{3}\s\d{3}\s\d{4}$', strip_whitespace=True)
    type: str | None = None
    user_id:UUID | None = None

class Address(BaseModel):
    street: str | None = None
    city: str | None = None
    state: str | None = None
    zip_code: str | None = None
    country: str | None = None
    user_id:UUID | None = None

class userCreate(UserBase):
    surname: str | None = None
    given: str | None = None
    middle: str | None = None
    title:str | None = None
    suffix:str | None = None
    phones:list[Phone]  = []
    addresses:list[Address] = []
    division:str | None = None
    department:str | None = None

class User(userCreate):
    display_name:str
    
    class Config:
        from_attributes = True

