from config.database import Session
from models.storegame_model import StoreGameModel as StoreGame
from schemas.storegame_model import StoreGame as StoreGameSchema

class StoreGameService:
    def __init__(self):
        self.db = Session()

    def create(self, store_game_data: StoreGame):
        new_store_game = StoreGame(**store_game_data.model_dump())
        self.db.add(new_store_game)
        self.db.commit()
        return { "message": "Store Game created" }

    def update(self, store_game_id: int, store_game_data: StoreGame):
        self.db.query(StoreGame).filter(StoreGame.id == store_game_id).update(store_game_data.model_dump())
        self.db.commit()
        return { "message": "Store Game updated" }

    def get_all(self):
        store_games = self.db.query(StoreGame).all()
        return store_games

    def get_by_id(self, store_game_id: int):
        store_game = self.db.query(StoreGame).filter(StoreGame.id == store_game_id).first()
        return store_game

    def delete(self, store_game_id: int):
        self.db.query(StoreGame).filter(StoreGame.id == store_game_id).delete()
        self.db.commit()
        return { "message": "Store Game deleted" }