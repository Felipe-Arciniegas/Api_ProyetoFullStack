from config.database import Session
from models.users import usersModel as Users
from schemas.users import users as UsersSchema

class UsersService:
    def __init__(self):
        self.db = Session()

    def create(self, users_data: Users):
        new_users = Users(**users_data.model_dump())
        self.db.add(new_users)
        self.db.commit()
        return { "message": "Users created" }

    def update(self, users_id: int, users_data: Users):
        self.db.query(Users).filter(Users.id == users_id).update(users_data.model_dump())
        self.db.commit()
        return { "message": "Users updated" }

    def get_all(self):
        users = self.db.query(Users).all()
        return users

    def get_by_id(self, users_id: int):
        users = self.db.query(Users).filter(Users.id == users_id).first()
        return users

    def delete(self, users_id: int):
        self.db.query(Users).filter(Users.id == users_id).delete()
        self.db.commit()
        return { "message": "Users deleted" }
