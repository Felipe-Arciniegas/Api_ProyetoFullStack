from config.database import Session
from models.game_library import GameLibraryModel as GameLibrary
from schemas.game_library import GameLibrary as GameLibrarySchema

class GameLibraryService:
    def __init__(self):
        self.db = Session()

    