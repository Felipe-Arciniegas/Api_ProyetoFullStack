from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class library(Base):
    __tablename__ = "library"

    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    games_id = Column(Integer, ForeignKey("store_game.id"))

    user = relationship("User", back_populates="library")
    game = relationship("StoreGame", back_populates="library")