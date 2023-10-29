from sqlalchemy import Column, Integer, String, Uuid, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, relationship
from uuid import uuid4

Base = declarative_base()

class Address(Base):
    __tablename__ = "addresses"

    addr_id = Column(Uuid, primary_key=True)
    type = Column(String, index=True)
    house_number = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)
    user_id = Column(Uuid, ForeignKey("users.user_id"))


class Phone(Base):
    __tablename__ = "phones"

    phone_id = Column(Uuid, primary_key=True)
    type = Column(String, index=True)
    phone = Column(String)
    user_id = Column(Uuid, ForeignKey("users", "users.user_id"))
    
class User(Base):
    __tablename__ = "users"

    user_id = Column(Uuid, primary_key=True, default=uuid4())
    display_name = Column(String)
    surname = Column(String, index=True)
    given = Column(String, index=True)
    middle = Column(String)
    title = Column(String)
    suffix = Column(String)
    phones:list[Phone] | None = Mapped[list[Phone]]
    addresses:list[Address] | None = Mapped[list[Address]]
    division = Column(String, index=True)
    department = Column(String, index=True)

