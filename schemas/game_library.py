from typing import Optional
from pydantic import BaseModel, Field

class GameLibrary(BaseModel):
    id: Optional[int] = None
    user_id: int = Field(ge=1)
    game_id: int = Field(ge=1)