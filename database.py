from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
# Database URL
DATABASE_URL = os.getenv('DATABASE_URL')
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Create a local database session
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Function to get the database session as a dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()