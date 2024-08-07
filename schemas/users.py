from typing import Optional
from pydantic import BaseModel, Field
import datetime

class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(min_length=5, max_length=50)
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)
    country: str = Field(min_length=5, max_length=50)
    creation_date: Optional[datetime.date] = Field(default=datetime.date.today(), ge=datetime.date.today())

class UserLogin(BaseModel):
    email: str = Field(min_length=5, max_length=50)
    password: str = Field(min_length=5, max_length=50)