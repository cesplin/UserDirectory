from sqlalchemy.orm import Session
import models, schemas
from uuid import UUID



def get_user(db:Session, user_id:UUID):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_all_users(db:Session):
    return db.query(schemas.User).all()

def add_user(db:Session, user:schemas.User):
    db_user = models.User(addresses=user.addresses, 
                          phones=user.phones, 
                          display_name=user.display_name, 
                          surname=user.suffix, 
                          given=user.given, 
                          middle=user.middle, 
                          department=user.department,
                          division=user.division,
                          title=user.title, 
                          suffix=user.suffix,
                          id=user.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user