from sqlalchemy import Column, String
from .data import Base
class login(Base):
    __tablename__ = "login"

    username = Column(String, primary_key=True, index=True)
    password = Column(String, index=True)

class rocks(Base):
    __tablename__ = "rocks"

    name = Column(String,primary_key=True,index=True)
    description = Column(String,index=True)
    image_url = Column(String,index=True)

class tags(Base):
    __tablename__ = "tags"

    name = Column(String,primary_key=True,index=True)
    tags = Column(String,primary_key=True,index=True)
