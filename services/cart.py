from config.database import Session
from models.cart import CartModel as Cart
from schemas.cart import Cart as CartSchema

class CartService:
    def __init__(self):
        self.db = Session()