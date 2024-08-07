from config.database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class StoreGame(Base):
    __tablename__ = "store_game"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True, index=True, nullable=False)
    overview = Column(String(500), nullable=False)
    price = Column(Float, nullable=False)
    release_date = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    category = Column(String(50), nullable=False)
    developer = Column(String(50), nullable=False)
    publisher = Column(String(50), nullable=False)

    cart = relationship("Cart", back_populates="game")
    game_library = relationship("Library", back_populates="game")