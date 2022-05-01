from sqlalchemy.orm import Session

from . import models, schemas

def get_items_crud(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item_crud(db: Session, id, item):
    db_item = db.query(models.Item).filter(models.Item.id == id).first()
    db_item.text = item["text"]
    db.commit()
    return db_item

def get_item_by_id_crud(db: Session, id: int):
    return db.query(models.Item).filter(models.Item.id == id).first()

def delete_item(db: Session, id: int):
    deleted_item = db.query(models.Item).filter_by(id=id).delete()
    db.commit()
    return deleted_item

