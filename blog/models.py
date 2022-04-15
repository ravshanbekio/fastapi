from .database import Base
from sqlalchemy import Column, Integer, String, Date

class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    author = Column(String)
    date = Column(Date)