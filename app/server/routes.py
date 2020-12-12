from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from .crud import (
    get_items_crud,
    create_item,
    get_item_by_id_crud,
    delete_item,
    update_item_crud
)

from .models import (
    Item,
)

from .schemas import (
    ItemCreate, Item
)

from .database import (
    get_db
)

router = APIRouter()


@router.post("/", response_description="Object data added into db")
def add_item(item: ItemCreate = Body(...), db: Session = Depends(get_db)):
    return create_item(db=db, item=item)


@router.get("/", response_description="Obj retrieved")
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = get_items_crud(db, skip, limit)
    if items:
        return items
    return []


@router.get("/{id}", response_description="Obj data retrieved")
def get_item(id, db: Session = Depends(get_db)):
    item = get_item_by_id_crud(db, id)
    if item:
        return item
    return HTTPException(status_code=404, detail="User not found")


@router.put("/{id}")
def update_obj_data(id: str, req: Item = Body(...), db: Session = Depends(get_db)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    print(req)
    updated_obj =  update_item_crud(db, id, req)
    if updated_obj:
        return {
            "data":  "Obj with ID: {} name update is successful".format(id),
            "message": "Obj updated successfully",}
    return HTTPException(
        "An error occurred",
        404,
        "There was an error updating the obj data.",
    )


@router.delete("/{id}", response_description="Obj data deleted from the database")
def remove_item(id: int, db: Session = Depends(get_db)):
    deleted_obj = delete_item(db, id)
    if deleted_obj:
        return {"data": "Obj with ID: {} removed".format(id), "message": "Obj deleted successfully"}
        
    return HTTPException(
        "An error occurred", 404, "Obj with id {0} doesn't exist".format(id)
    )
