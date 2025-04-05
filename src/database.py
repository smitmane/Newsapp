from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "mysql+pymysql://root:Root%401234@localhost:3306/my_database"
# DATABASE_URL = f"mysql+pymysql://{os.getenv("MYSQL_USER","root")}:{os.getenv("MYSQL_PWD","Root%401234")}@{os.getenv("MYSQL_HOST","localhost")}:{os.getenv("MYSQL_Port","3306")}/{os.getenv("MYSQL_DB","my_database")}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
