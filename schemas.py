from sqlalchemy import Column, Integer, String, Uuid
from sqlalchemy.orm import declarative_base, Mapped
from uuid import uuid4

Base = declarative_base()



class Address(Base):
    __tablename__ = "addresses"

    addr_id = Column(Uuid, primary_key=True, default=uuid4())
    type = Column(String, index=True)
    house_number = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    postal_code = Column(String)

class Phone(Base):
    __tablename__ = "phones"

    phone_id = Column(Uuid, primary_key=True, default=uuid4())
    type = Column(String, index=True)
    phone = Column(String)

class User(Base):
    __tablename__ = "users"

    user_id = Column(Uuid, primary_key=True, default=uuid4())
    display_name = Column(String)
    surname = Column(String, index=True)
    given = Column(String, index=True)
    middle = Column(String)
    title = Column(String)
    suffix = Column(String)
    phones = Mapped[list[Phone]]
    addresses = Mapped[list[Address]]
    division = Column(String, index=True)
    department = Column(String, index=True)

