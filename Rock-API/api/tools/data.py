from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except: 
    pass
SQLALCHEMY_DATABASE_URL = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()