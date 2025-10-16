from beanie import Document
from pydantic import EmailStr, Field
from typing import Annotated
from beanie import Indexed
from uuid import uuid4

class User(Document):
    # id string que será gravado no campo _id do Mongo
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=8, max_length=20)
    email: Annotated[EmailStr, Indexed(unique=True)]
    password: str = Field(..., min_length=6, max_length=72)

    class Settings:
        name = "users"

    class Config:
        # populate_by_name permite trabalhar com 'id' em vez de '_id'
        populate_by_name = True
