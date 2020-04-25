import database as db
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base


base = declarative_base()


class Item(base):
    __tablename__ = 'item'
    no = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)

    def get_item(self):
        session = db.create_session()
        item_list = session.query(Item).all()
        if item_list is None:
            return []
        return item_list
