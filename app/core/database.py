from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


load_dotenv()
ugc_db = os.getenv("DATABASE_URL")
assert ugc_db is not None, "DATABASE_URL is missing from .env"

engine = create_engine(ugc_db)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind=engine)

Base = declarative_base()