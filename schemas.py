from sqlalchemy import Column, Integer, String, Uuid, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, relationship, mapped_column
from typing import Optional
from uuid import uuid4,UUID

Base = declarative_base()

class Address(Base):
    __tablename__ = "addresses"

    addr_id:Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    type:Mapped[Optional[str]]
    house_number:Mapped[Optional[str]]
    street:Mapped[Optional[str]]
    city:Mapped[Optional[str]]
    state:Mapped[Optional[str]]
    postal_code:Mapped[Optional[str]]
    user_id:Mapped[UUID] = mapped_column(ForeignKey('users.user_id'))
    user:Mapped["User"] = relationship(back_populates='')

    def __repr__(self) -> str:
        return f"Address(addr_id={self.addr_id}, type={self.type}, house_number={self.house_number}, street = {self.street}, city={self.city}, state={self.state}, postal_code={self.postal_code}, user_id={self.user_id})"


class Phone(Base):
    __tablename__ = "phones"

    phone_id:Mapped[UUID] = mapped_column(primary_key=True,default=uuid4)
    type:Mapped[Optional[str]] = mapped_column(index=True)
    phone:Mapped[Optional[str]]
    user_id:Mapped[UUID] = mapped_column(ForeignKey('users.user_id'))
    user: Mapped['User'] = relationship(back_populates="phones")

    def __repr__(self) -> str:
        return f"Phone(phone_id={self.phone_id}, type={self.type}, user_id={self.user_id})"
    
class User(Base):
    __tablename__ = "users"

    user_id:Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    display_name:Mapped[str] = mapped_column(index=True)
    surname:Mapped[Optional[str]] = mapped_column(index=True)
    given:Mapped[Optional[str]] = mapped_column(index=True)
    middle:Mapped[Optional[str]]
    title:Mapped[Optional[str]]
    suffix:Mapped[Optional[str]]
    phones:Mapped[list['Phone']] = relationship(back_populates="user")
    addresses:Mapped[list['Address']] = relationship(back_populates="user")
    division:Mapped[Optional[str]]
    department:Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(user_id={self.user_id}, display_name={self.display_name}, surname={self.surname}, given={self.given}, middle={self.middle}, title={self.title}, suffix={self.suffix}, phones={self.phones}, addresses={self.addresses}, division={self.division}, department={self.department})"
    

