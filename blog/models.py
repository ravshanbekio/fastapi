from sqlalchemy import Column, Integer, String
from .database import Base

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    author = Column(String)

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    country = Column(String)