from sqlalchemy import Column, String

from webapp_kit.persistence import BaseDBEntity


class User(BaseDBEntity):
    __tablename__ = "usersdb"

    name = Column(String)