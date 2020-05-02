import database as db
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


base = declarative_base()


class Item(base):
    # テーブル情報
    __tablename__ = 'item'
    no = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)

    def get_item(self):
        """ itemテーブルの全データを取得 """
        session = db.create_session()
        item_list = session.query(Item).all()
        if item_list is None:
            return []
        return item_list

    def register_item(self, item=None):
        """ itemテーブル登録 """
        session = db.create_session()
        session.add(item)
        session.commit()

    def get_maxno(self):
        """ 最大のitem.noを取得 """
        session = db.create_session()
        max_no = session.query(func.max(Item.no, label='no')).one()
        return max_no