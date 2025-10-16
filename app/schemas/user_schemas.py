from typing import Optional
from pydantic import BaseModel, EmailStr, Field, field_serializer
from bson import ObjectId

# ---------- CREATE ----------
class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=8, max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)

# ---------- UPDATE ----------
class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=100)
    phone: Optional[str] = Field(None, min_length=8, max_length=20)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6, max_length=72)
# ---------- OUTPUT ----------
class UserOut(BaseModel):
    id: str
    name: str
    phone: str
    email: EmailStr

    @field_serializer("id")
    def serialize_id(self, id_value: ObjectId, _info):
        return str(id_value)

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2
