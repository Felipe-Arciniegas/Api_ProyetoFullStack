from typing import Optional
from pydantic import BaseModel, Field
import datetime

class Cart(BaseModel):
    id: Optional[int] = None
    user_id: int = Field(ge=1)
    game_id: int = Field(ge=1)
    quantity: int = Field(gt=0)
    date: Optional[datetime.datetime] = Field(default=datetime.datetime.now(datetime.UTC))