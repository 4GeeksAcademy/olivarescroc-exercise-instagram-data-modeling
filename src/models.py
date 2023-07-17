import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum

Base = declarative_base() #declaración de la base de sqlalchemy

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    username = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    comment = relationship('Comment')           #Relación User -> Comment /one to many
    post = relationship('Post')                  #Relación Post -> Comment /one to many


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment')
    media = relationship('Media')


class MediaEnum(enum.Enum):
    mp4 = 'mp4'
    gif = 'gif'
    jpg = 'jpg'


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaEnum), nullable=False)
    url = Column(String(250), nullable=False )
    post_id = Column(Integer, ForeignKey('post.id'))


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    comment_from_id = Column(Integer, ForeignKey('user.id'))
    comment_to_id = Column(Integer, ForeignKey('user.id'))




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
