from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    text: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True