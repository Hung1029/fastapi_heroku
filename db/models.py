from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbArticle(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sku = Column(String)
    description = Column(String)
    description_long = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates ='created_articles')


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_admin = Column(Boolean)
    created_articles = relationship('DbArticle', back_populates='owner')



