from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url_database = 'postgresql://odoo:odoo@localhost:5432/fastapi_test'

engine = create_engine(url_database)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()