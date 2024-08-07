from config.database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    

    cart = relationship("Cart", back_populates="game")
    game_library = relationship("Library", back_populates="game")