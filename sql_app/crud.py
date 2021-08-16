from sqlalchemy.orm import Session

from . import models

def get_data(db: Session, id: int):
    return db.query(models.Data).filter(models.Data.id == id).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Data).offset(skip).limit(limit).all()

def get_text(db: Session):
    return db.query(models.Data.text).all()

def get_label(db: Session):
    return db.query(models.Data.label).all()
