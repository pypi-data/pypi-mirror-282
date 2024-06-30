from sqlalchemy import Column, String

from webapp_kit.persistence import BaseDBEntity


class SettingsDB(BaseDBEntity):
    __tablename__ = "settingsdb"

    test = Column(String)