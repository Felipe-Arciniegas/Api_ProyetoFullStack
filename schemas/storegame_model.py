from typing import Optional
from pydantic import BaseModel, Field

class StoreGame(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=5, max_length=500)
    price: float = Field(ge=0)
    release_date: str = Field(min_length=5, max_length=50)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5, max_length=50)
    developer: str = Field(min_length=5, max_length=50)
    publisher: str = Field(min_length=5, max_length=50)


