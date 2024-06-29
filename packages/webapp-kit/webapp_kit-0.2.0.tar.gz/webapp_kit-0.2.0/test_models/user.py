from sqlalchemy import Column, String

from src.persistence import BaseDBEntity


class User(BaseDBEntity):
    __tablename__ = "usersdb"

    name = Column(String)