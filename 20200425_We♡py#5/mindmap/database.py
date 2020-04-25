import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import SystemConfig


def create_session():
    engine = create_engine(SystemConfig.SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine)
    return session()
