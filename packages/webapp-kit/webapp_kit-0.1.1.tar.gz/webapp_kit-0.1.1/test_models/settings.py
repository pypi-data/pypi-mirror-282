from sqlalchemy import Column, String

from src.persistence import BaseDBEntity


class SettingsDB(BaseDBEntity):
    __tablename__ = "settingsdb"

    test = Column(String)