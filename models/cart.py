from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Cart(Base):
    __tablename__ = "cart"

    id = Column(Integer, primary_key=True, index=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    games_id = Column(Integer, ForeignKey("store_game.id"))
    price_id = Column(Integer, ForeignKey("store_game.price"))
    date = Column(DateTime, default=datetime.datetime.utcnow())

    game = relationship("StoreGame", back_populates="cart")
    price = relationship("StoreGame", back_populates="cart")